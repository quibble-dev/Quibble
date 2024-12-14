from http import HTTPMethod

from django.shortcuts import get_object_or_404
from rest_framework import response, status, viewsets
from rest_framework.decorators import action

from apps.comment.api.v1.serializers import CommentSerializer

from ...models import QuibModel
from .serializers import QuibSerializer, QuibSlimSerializer


class QuibModelViewSet(viewsets.ModelViewSet):
    queryset = QuibModel.objects.all()

    def get_serializer_class(self):  # pyright: ignore
        if self.action == 'list':
            return QuibSlimSerializer
        # if custom action: 'comment'
        if self.action == 'comment':
            return CommentSerializer
        return QuibSerializer

    @action(detail=True, methods=[HTTPMethod.POST])
    def comment(self, request, pk=None):
        quib_instance = get_object_or_404(QuibModel, pk=pk)

        serializer = CommentSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        comment_instance = serializer.save()
        quib_instance.comments.add(comment_instance)

        return response.Response(status=status.HTTP_201_CREATED, data=serializer.data)
