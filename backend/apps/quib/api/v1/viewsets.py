from http import HTTPMethod

from django.shortcuts import get_object_or_404
from rest_framework import response, status, viewsets
from rest_framework.decorators import action

from apps.comment.api.v1.serializers import CommentSerializer

from ...models import Quib
from .serializers import QuibSerializer, QuibSlimSerializer


class QuibViewSet(viewsets.ModelViewSet):
    queryset = Quib.objects.all()

    def get_serializer_class(self):  # pyright: ignore
        if self.action == 'list':
            return QuibSlimSerializer
        # if custom action: 'comment'
        if self.action == 'comments':
            return CommentSerializer
        return QuibSerializer

    @action(detail=True, methods=[HTTPMethod.GET, HTTPMethod.POST])
    def comments(self, request, pk=None):
        quib_instance = get_object_or_404(Quib, pk=pk)

        if request.method == HTTPMethod.GET:
            comments = quib_instance.comments.all()
            serializer = CommentSerializer(comments, many=True)

            return response.Response(serializer.data, status=status.HTTP_200_OK)

        serializer = CommentSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        comment_instance = serializer.save()
        quib_instance.comments.add(comment_instance)

        return response.Response(serializer.data, status=status.HTTP_201_CREATED)
