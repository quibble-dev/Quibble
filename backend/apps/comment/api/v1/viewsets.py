from common.api.bases.viewsets import UpdateRetrieveDestroyViewSet

from ...models import Comment
from .serializers import CommentDetailSerializer


class CommentViewSet(UpdateRetrieveDestroyViewSet):
    queryset = Comment.objects.all()
    serializer_class = CommentDetailSerializer

    def perform_destroy(self, instance):
        Comment.objects.soft_delete(instance)  # pyright: ignore
        # perform cleanup
        Comment.objects.clean_up_soft_deleted()  # pyright: ignore
