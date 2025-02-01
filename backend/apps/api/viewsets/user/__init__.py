from http import HTTPMethod
from itertools import chain

from django.conf import settings
from django.db.models import CharField, Value
from django.http import Http404
from django.shortcuts import get_object_or_404
from rest_framework import exceptions, filters, permissions, response, status, viewsets
from rest_framework.decorators import action

from apps.comment.models import Comment
from apps.post.models import Post
from apps.user.models import Profile

from ...serializers.user.profile import ProfileSerializer
from ...serializers.user.profile.overview import OverviewSerializer


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

    @action(detail=False, methods=[HTTPMethod.GET], url_path=r'(?P<username>[^/.]+)/overview')
    def overview(self, request, username=None):
        """Returns a mixed list of posts and comments by the user, ordered by date."""
        try:
            profile = get_object_or_404(Profile, username=username)

            posts = (
                Post.objects.filter(poster=profile)
                .annotate(type=Value("post", CharField()))
                .order_by('-created_at')
            )
            comments = (
                Comment.objects.with_annotated_ratio()
                .filter(commenter=profile)
                .annotate(type=Value("comment", CharField()))
                .order_by('-created_at')
            )

            post_data = OverviewSerializer(posts, many=True).data
            comment_data = OverviewSerializer(comments, many=True).data

            combined_data = sorted(
                chain(post_data, comment_data), key=lambda x: x['data']['created_at'], reverse=True
            )

            return response.Response(combined_data, status=status.HTTP_200_OK)

        except Http404:
            raise exceptions.NotFound(
                detail="No Profile matches the given query.", code=status.HTTP_404_NOT_FOUND
            )


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
