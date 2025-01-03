from http import HTTPMethod

from django.shortcuts import get_object_or_404
from drf_spectacular.utils import extend_schema
from rest_framework import response, status, viewsets
from rest_framework.decorators import action

from apps.comment.api.v1.serializers import (
    CommentCreateSerializer,
    CommentDetailSerializer,
)

from ...models import Quib
from .serializers import QuibSerializer


class QuibViewSet(viewsets.ModelViewSet):
    queryset = Quib.objects.all()
    serializer_class = QuibSerializer

    def get_serializer_class(self):  # pyright: ignore
        # if custom action: 'comment'
        if self.action == 'comments':
            return CommentCreateSerializer
        return self.serializer_class

    @extend_schema(responses=CommentDetailSerializer(many=True))
    @action(detail=True, methods=[HTTPMethod.GET, HTTPMethod.POST])
    def comments(self, request, pk=None):
        quib_instance = get_object_or_404(Quib, pk=pk)

        context = {'request': request}

        if request.method == HTTPMethod.GET:
            comments = quib_instance.comments.with_annotated_ratio()  # pyright: ignore
            serializer = CommentDetailSerializer(comments, many=True, context=context)

            return response.Response(serializer.data, status=status.HTTP_200_OK)

        serializer = CommentCreateSerializer(data=request.data, context=context)
        serializer.is_valid(raise_exception=True)

        comment_instance = serializer.save()
        quib_instance.comments.add(comment_instance)

        return response.Response(serializer.data, status=status.HTTP_201_CREATED)
