from django.contrib.auth import login
from rest_framework import viewsets, permissions, filters, views
from rest_framework.decorators import action
from rest_framework.exceptions import ValidationError
from rest_framework.response import Response
from knox.views import LoginView as KnoxLoginView

from .models import Profile, User
from .serializers import (
    AuthSerializer,
    CustomAuthTokenSerializer,
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


class LoginView(KnoxLoginView):
    """
    Customized Knox login view to handle authentication with email and password.

    This view authenticates the user using email and password credentials
    and issues a Knox token upon successful login.

    Overrides:
    - `post`: Validates user credentials and returns an authentication token.

    Permission:
    - Allows access to unauthenticated users (public endpoint).
    """

    serializer_class = AuthSerializer
    permission_classes = (permissions.AllowAny,)

    def post(self, request, format=None):
        """
        Authenticate user and generate an authentication token.

        Args:
            request: The HTTP request containing email and password data.
            format: Optional format specifier for the response.

        Returns:
            Response containing the Knox token upon successful authentication.
        """
        serializer = CustomAuthTokenSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data['user']
        login(request, user)
        return super().post(request, format=None)


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
        if user.profiles.count() >= 5:
            raise ValidationError('A user cannot have more than 5 profiles')
        serializer.save(user=user)
