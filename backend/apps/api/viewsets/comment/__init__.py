from apps.comment.models import Comment

from ...bases.viewsets import UpdateRetrieveDestroyViewSet
from ...serializers.comment import CommentDetailSerializer


class CommentViewSet(UpdateRetrieveDestroyViewSet):
    queryset = Comment.objects.with_annotated_ratio()
    serializer_class = CommentDetailSerializer

    def perform_destroy(self, instance):
        Comment.objects.soft_delete(instance)  # pyright: ignore
        # perform cleanup
        Comment.objects.clean_up_soft_deleted()  # pyright: ignore
