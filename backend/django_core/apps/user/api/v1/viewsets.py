from django.conf import settings
from rest_framework import exceptions, permissions, viewsets, filters

from django_core.apps.user.models import Profile, User
from .serializers import (
    ProfileSerializer,
    UserSerializer,
)


class UserViewSet(viewsets.ReadOnlyModelViewSet):
    """
    ViewSet for performing read-only operations on the User model.

    Additional Actions:
    - `<user_id>/profiles`: Retrieve all profiles associated with a specific user.
    """

    queryset = User.objects.all()
    serializer_class = UserSerializer


class ProfileViewSet(viewsets.ReadOnlyModelViewSet):
    """
    ViewSet for performing read-only operations on the Profile model.

    Filtering:
    - Allows searching profiles by username.
    """

    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer
    filter_backends = (filters.SearchFilter,)
    search_fields = ('username',)


class MyProfilesViewSet(viewsets.ModelViewSet):
    """
    ViewSet to manage profiles associated with the authenticated user.

    Permissions:
    - Requires user authentication to access and modify profiles.
    """

    permission_classes = (permissions.IsAuthenticated,)
    serializer_class = ProfileSerializer

    def get_queryset(self):  # pyright: ignore [reportIncompatibleMethodOverride]
        """
        Restrict queryset to profiles owned by the currently authenticated user.
        """
        # during schema generation
        if getattr(self, 'swagger_fake_view', False):
            return Profile.objects.none()
        user = self.request.user
        return user.profiles.all()

    def perform_create(self, serializer):
        """
        Create a new profile for the authenticated user, enforcing a maximum limit.

        Raises:
            ValidationError: If the user already has 5 profiles.
        """
        user = self.request.user
        if user.profiles.count() >= settings.PROFILE_LIMIT:
            raise exceptions.ValidationError('A user cannot have more than 5 profiles')
        serializer.save(user=user)
