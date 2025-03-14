from apps.api.bases.serializers import ReactionSerializer
from apps.comment.models import Comment
from mixins.api.reaction import ReactionMixin

from ...bases.viewsets import UpdateRetrieveDestroyViewSet
from ...serializers.comment import CommentDetailSerializer


class CommentViewSet(ReactionMixin, UpdateRetrieveDestroyViewSet):
    queryset = Comment.objects.with_ratio()
    serializer_class = CommentDetailSerializer

    # extra custom serializers
    serializer_classes = {
        # extra actions
        'reaction': ReactionSerializer,
    }

    def get_serializer_class(self):
        if self.action in self.serializer_classes:
            return self.serializer_classes[self.action]
        return self.serializer_class

    def perform_destroy(self, instance):
        Comment.objects.soft_delete(instance)
        # perform cleanup
        Comment.objects.clean_up_soft_deleted()
