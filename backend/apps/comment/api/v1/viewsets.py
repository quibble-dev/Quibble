from common.api.bases.viewsets import UpdateRetrieveDestroyViewSet

from ...models import CommentModel
from .serializers import CommentSerializer


class CommentModelViewSet(UpdateRetrieveDestroyViewSet):
    queryset = CommentModel.objects.all()
    serializer_class = CommentSerializer

    def perform_destroy(self, instance):
        CommentModel.objects.soft_delete(instance)  # pyright: ignore
        # perform cleanup
        CommentModel.objects.clean_up_soft_deleted()  # pyright: ignore
