from django.contrib.auth import login

from rest_framework import viewsets, permissions, filters
from rest_framework.decorators import action
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
    CRUD operations for User model
    """

    queryset = User.objects.all()
    serializer_class = UserSerializer

    @action(detail=True)
    def profiles(self, request, pk=None):
        """
        Show all profiles associated with specific user
        """

        user = self.get_object()
        user_profiles = user.profiles.all()
        serializer = ProfileSerializer(user_profiles, many=True)

        return Response(serializer.data)


class ProfileViewSet(viewsets.ModelViewSet):
    """
    CRUD operations for Profile model
    """

    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer
    filter_backends = (filters.SearchFilter,)
    search_fields = ('username',)


class LoginView(KnoxLoginView):
    """
    Customized knox LoginView with email and password
    """

    serializer_class = AuthSerializer
    permission_classes = (permissions.AllowAny,)

    def post(self, request, format=None):
        serializer = CustomAuthTokenSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        user = serializer.validated_data['user']
        login(request, user)

        return super().post(request, format=None)
