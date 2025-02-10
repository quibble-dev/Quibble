from http import HTTPMethod
from typing import cast

from drf_spectacular.utils import extend_schema
from rest_framework import exceptions, response
from rest_framework.decorators import action

from apps.api.http import HttpRequest
from apps.comment.models import Comment

from ...bases.viewsets import UpdateRetrieveDestroyViewSet
from ...serializers.comment import CommentDetailSerializer
from ...serializers.comment.reaction import CommentReactionResponseSerializer


class CommentViewSet(UpdateRetrieveDestroyViewSet):
    queryset = Comment.objects.with_annotated_ratio()
    serializer_class = CommentDetailSerializer

    def get_object(self) -> Comment:
        return super().get_object()

    @extend_schema(request=None, responses=CommentReactionResponseSerializer)
    @action(detail=True, methods=[HTTPMethod.PATCH])
    def reaction(self, request: HttpRequest, pk=None):
        """
        This endpoint allows a user to either upvote or downvote a comment.

        Query Parameters:
        - `action` (str): Either `"upvote"` or `"downvote"`.

        Responses:
        - `200 OK`: Reaction applied successfully. Returns `{"success": True}`.
        - `400 Bad Request`: If the user has already applied the same reaction or an invalid action is provided.
        """
        action = request.GET.get('action')
        comment = self.get_object()
        req_user = cast(HttpRequest, self.request).user_profile

        if action == 'upvote':
            if req_user and comment.upvotes.filter(pk=req_user.pk).exists():
                raise exceptions.ValidationError('You have already upvoted this comment.')

            comment.downvotes.remove(req_user)
            comment.upvotes.add(req_user)
        elif action == 'downvote':
            if req_user and comment.downvotes.filter(pk=req_user.pk).exists():
                raise exceptions.ValidationError('You have already downvoted this comment.')

            comment.upvotes.remove(req_user)
            comment.downvotes.add(req_user)
        else:
            raise exceptions.ValidationError(f'Invalid action: {action}')

        return response.Response({'success': True})

    def perform_destroy(self, instance):
        Comment.objects.soft_delete(instance)
        # perform cleanup
        Comment.objects.clean_up_soft_deleted()
