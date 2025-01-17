from django.conf import settings
from rest_framework import exceptions, filters, permissions, viewsets

from apps.user.models import Profile

from ...serializers.user.profile import ProfileSerializer


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

    def get_queryset(self):  # pyright: ignore
        """
        Restrict queryset to profiles owned by the currently authenticated user.
        """
        # during schema generation
        if getattr(self, 'swagger_fake_view', False):
            return Profile.objects.none()
        user = self.request.user
        return user.profiles.all()  # pyright: ignore

    def perform_create(self, serializer):
        """
        Create a new profile for the authenticated user, enforcing a maximum limit.

        Raises:
            ValidationError: If the user already has limited profiles.
        """
        user = self.request.user
        if user.profiles.count() >= settings.PROFILE_LIMIT:  # pyright: ignore
            raise exceptions.ValidationError(
                f'A user cannot have more than {settings.PROFILE_LIMIT} profiles.'
            )
        serializer.save(user=user)
