from http import HTTPMethod
from typing import cast

from drf_spectacular.utils import extend_schema
from rest_framework import exceptions, response
from rest_framework.decorators import action

from apps.api.bases.serializers import SuccessResponseSerializer
from apps.api.http import HttpRequest
from apps.comment.models import Comment

from ...bases.viewsets import UpdateRetrieveDestroyViewSet
from ...serializers.comment import CommentDetailSerializer
from ...serializers.comment.reaction import CommentReactionSerializer


class CommentViewSet(UpdateRetrieveDestroyViewSet):
    queryset = Comment.objects.with_annotated_ratio()
    serializer_class = CommentDetailSerializer

    # extra custom serializers
    serializer_classes = {
        # extra actions
        'reaction': CommentReactionSerializer,
    }

    def get_serializer_class(self):
        if self.action in self.serializer_classes:
            return self.serializer_classes[self.action]
        return self.serializer_class

    def get_object(self) -> Comment:
        return super().get_object()

    @extend_schema(responses=SuccessResponseSerializer)
    @action(detail=True, methods=[HTTPMethod.PATCH])
    def reaction(self, request, pk=None):
        """
        This endpoint allows a user to either upvote or downvote a comment.

        Request Body:
        - `action` (str): Either `"upvote"` or `"downvote"`.

        Responses:
        - `200 OK`: Reaction applied successfully. Returns `{"success": True}`.
        - `400 Bad Request`: If the user has already applied the same reaction or an invalid action is provided.
        """
        serializer = CommentReactionSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        action = serializer.validated_data['action']

        comment = self.get_object()
        req_user = cast(HttpRequest, self.request).user_profile

        if not req_user:
            raise exceptions.NotAuthenticated()

        if action == 'upvote':
            if req_user and comment.upvotes.filter(pk=req_user.pk).exists():
                comment.upvotes.remove(req_user)
                return response.Response({'success': True})

            comment.downvotes.remove(req_user)
            comment.upvotes.add(req_user)
        elif action == 'downvote':
            if comment.downvotes.filter(pk=req_user.pk).exists():
                comment.downvotes.remove(req_user)
                return response.Response({'success': True})

            comment.upvotes.remove(req_user)
            comment.downvotes.add(req_user)

        return response.Response({'success': True})

    def perform_destroy(self, instance):
        Comment.objects.soft_delete(instance)
        # perform cleanup
        Comment.objects.clean_up_soft_deleted()
