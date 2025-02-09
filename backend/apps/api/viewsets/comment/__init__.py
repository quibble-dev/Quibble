from http import HTTPMethod
from typing import cast

from rest_framework import response
from rest_framework.decorators import action

from apps.api.http import HttpRequest
from apps.comment.models import Comment

from ...bases.viewsets import UpdateRetrieveDestroyViewSet
from ...serializers.comment import CommentDetailSerializer


class CommentViewSet(UpdateRetrieveDestroyViewSet):
    queryset = Comment.objects.with_annotated_ratio()
    serializer_class = CommentDetailSerializer

    def get_object(self) -> Comment:
        return super().get_object()

    @action(detail=True, methods=[HTTPMethod.PATCH])
    def upvote(self, request, pk=None):
        comment = self.get_object()
        req_user = cast(HttpRequest, self.request).user_profile

        comment.downvotes.remove(req_user)
        comment.upvotes.add(req_user)

        return response.Response({'success': True})

    def perform_destroy(self, instance):
        Comment.objects.soft_delete(instance)
        # perform cleanup
        Comment.objects.clean_up_soft_deleted()
