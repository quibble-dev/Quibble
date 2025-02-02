from http import HTTPMethod
from itertools import chain

from django.conf import settings
from django.db.models import CharField, QuerySet, Value
from drf_spectacular.utils import extend_schema
from rest_framework import exceptions, filters, permissions, response, viewsets
from rest_framework.decorators import action

from apps.user.models import Profile

from ...serializers.user.profile import ProfileSerializer
from ...serializers.user.profile.overview import OverviewSerializer


@extend_schema(tags=["user & profiles"])
class ProfileViewSet(viewsets.ReadOnlyModelViewSet):
    """
    ViewSet for performing read-only operations on the Profile model.

    Filtering:
    - Allows searching profiles by username.
    """

    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer
    filter_backends = (filters.SearchFilter,)
    search_fields = ("username",)

    serializer_classes = {
        "overview": OverviewSerializer,
    }

    def get_serializer_class(self):
        if self.action in self.serializer_classes:
            return self.serializer_classes[self.action]
        return self.serializer_class

    def get_queryset(self) -> QuerySet[Profile]:
        return super().get_queryset()

    def get_object(self) -> Profile:
        qs = self.get_queryset()
        filter_kwargs = {f"{self.lookup_field}": self.kwargs[self.lookup_field]}
        obj = qs.filter(**filter_kwargs).first()

        if not obj:
            raise exceptions.NotFound(
                f"Profile with ID {self.kwargs[self.lookup_field]} not found."
            )
        return obj

    @extend_schema(responses=OverviewSerializer(many=True))
    @action(detail=True, methods=[HTTPMethod.GET])
    def overview(self, request, pk=None):
        """Returns a mixed list of posts and comments by the user, ordered by date."""
        profile = self.get_object()
        posts = profile.posts.all().annotate(type=Value("post", CharField()))
        comments = profile.comments.with_annotated_ratio().annotate(
            type=Value("comment", CharField())
        )

        combined_data = sorted(chain(posts, comments), key=lambda obj: obj.created_at, reverse=True)
        serialized_data = self.get_serializer(
            combined_data, context={'request': request}, many=True
        ).data
        return response.Response(serialized_data)


@extend_schema(tags=["user & profiles"])
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
        if getattr(self, "swagger_fake_view", False):
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
                f"A user cannot have more than {settings.PROFILE_LIMIT} profiles."
            )
        serializer.save(user=user)
