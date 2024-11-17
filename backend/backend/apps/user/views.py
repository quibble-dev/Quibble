from django.conf import settings
from django.contrib.auth import authenticate
from rest_framework import viewsets, permissions, filters, views
from rest_framework import exceptions
from rest_framework.authtoken.models import Token
from rest_framework.decorators import action
from rest_framework.exceptions import ValidationError
from rest_framework.response import Response

from core.exceptions import ServerError

from .models import Profile, User
from .serializers import (
    ProfileSerializer,
    UserSerializer,
)


class UserViewSet(viewsets.ModelViewSet):
    """
    ViewSet for performing CRUD operations on the User model.

    Additional Actions:
    - `<user_id>/profiles`: Retrieve all profiles associated with a specific user.
    """

    queryset = User.objects.all()
    serializer_class = UserSerializer

    @action(detail=True)
    def profiles(self, request, pk=None):
        """
        Retrieve all profiles associated with a specific user.

        Returns:
            Response containing serialized profile data for the user.
        """
        user = self.get_object()
        user_profiles = user.profiles.all()
        serializer = ProfileSerializer(user_profiles, many=True)
        return Response(serializer.data)


class ProfileViewSet(viewsets.ModelViewSet):
    """
    ViewSet for performing CRUD operations on the Profile model.

    Filtering:
    - Allows searching profiles by username.
    """

    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer
    filter_backends = (filters.SearchFilter,)
    search_fields = ('username',)


class LoginView(views.APIView):
    """
    Customized drf basic token authentication.

    This view authenticates the user using email and password credentials
    and issues a token upon successful login.
    """

    def post(self, request, format=None):
        user = authenticate(
            email=request.data.get('email'), password=request.data.get('password')
        )
        if user:
            token, _ = Token.objects.get_or_create(user=user)
            return Response({'token': token.key})
        else:
            raise exceptions.AuthenticationFailed()


class LogoutView(views.APIView):
    """
    View to handle user logout by deleting the authentication token.
    """

    permission_classes = (permissions.IsAuthenticated,)

    def post(self, request, format=None):
        try:
            Token.objects.filter(user=request.user).delete()
            return Response({'detail': 'Successfully logged out.'})

        except Exception as e:
            raise ServerError(detail=f"An error occurred while logging out: {str(e)}")


class MeView(views.APIView):
    """
    View to retrieve information for the currently authenticated user.

    - `get`: Returns the details of the authenticated user based on their token.

    Permission:
    - Requires user authentication.
    """

    permission_classes = (permissions.IsAuthenticated,)

    def get(self, request):
        """
        Retrieve the currently authenticated user's profile information.

        Args:
            request: The HTTP request made by the authenticated user.

        Returns:
            Response containing serialized data for the authenticated user.
        """
        serializer = UserSerializer(request.user)
        return Response(serializer.data)


class MyProfilesViewSet(viewsets.ModelViewSet):
    """
    ViewSet to manage profiles associated with the authenticated user.

    Permissions:
    - Requires user authentication to access and modify profiles.
    """

    permission_classes = (permissions.IsAuthenticated,)
    serializer_class = ProfileSerializer

    def get_queryset(self):
        """
        Restrict queryset to profiles owned by the currently authenticated user.

        Returns:
            Queryset containing profiles that belong to the authenticated user.
        """
        user = self.request.user
        return user.profiles.all()

    def perform_create(self, serializer):
        """
        Create a new profile for the authenticated user, enforcing a maximum limit.

        Raises:
            ValidationError: If the user already has 5 profiles.

        Args:
            serializer: The serializer instance containing profile data.

        Returns:
            None
        """
        user = self.request.user
        if user.profiles.count() >= settings.PROFILE_LIMIT:
            raise ValidationError('A user cannot have more than 5 profiles')
        serializer.save(user=user)
