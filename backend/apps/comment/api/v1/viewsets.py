from rest_framework import viewsets

from ...models import CommentModel
from .serializers import CommentSerializer


class CommentModelViewSet(viewsets.ModelViewSet):
    queryset = CommentModel.objects.all()
    serializer_class = CommentSerializer

    def perform_destroy(self, instance):
        CommentModel.objects.soft_delete(instance)  # pyright: ignore
