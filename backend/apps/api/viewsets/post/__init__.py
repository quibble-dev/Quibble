from http import HTTPMethod

from django.shortcuts import get_object_or_404
from drf_spectacular.utils import extend_schema
from rest_framework import response, status, viewsets
from rest_framework.decorators import action

from apps.post.models import Post

from ...serializers.comment import CommentCreateSerializer, CommentDetailSerializer
from ...serializers.post import PostSerializer


class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer

    def get_serializer_class(self):  # pyright: ignore
        # if custom action: 'comment'
        if self.action == 'comments':
            return CommentCreateSerializer
        return self.serializer_class

    @extend_schema(responses=CommentDetailSerializer(many=True))
    @action(detail=True, methods=[HTTPMethod.GET, HTTPMethod.POST])
    def comments(self, request, pk=None):
        post_instance = get_object_or_404(Post, pk=pk)

        context = {'request': request}

        if request.method == HTTPMethod.GET:
            comments = post_instance.comments.with_annotated_ratio()  # pyright: ignore
            serializer = CommentDetailSerializer(comments, many=True, context=context)

            return response.Response(serializer.data, status=status.HTTP_200_OK)

        serializer = CommentCreateSerializer(data=request.data, context=context)
        serializer.is_valid(raise_exception=True)

        comment_instance = serializer.save()
        post_instance.comments.add(comment_instance)
        # hard-code ratio
        comment_instance.ratio = 1

        response_serializer = CommentDetailSerializer(comment_instance, context=context)
        return response.Response(response_serializer.data, status=status.HTTP_201_CREATED)
