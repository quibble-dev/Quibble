from rest_framework import viewsets

from ...models import CommentModel
from .serializers import CommentSerializer


class CommentViewSet(viewsets.ModelViewSet):
    queryset = CommentModel.objects.all()
    serializer_class = CommentSerializer
