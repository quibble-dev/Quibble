from apps.api.bases.serializers import ReactionSerializer
from apps.comment.models import Comment
from mixins.api.reaction import ReactionMixin

from ...bases.viewsets import UpdateRetrieveDestroyViewSet
from ...serializers.comment import CommentSerializer


class CommentViewSet(ReactionMixin, UpdateRetrieveDestroyViewSet):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer

    serializer_mapping = {
        'reaction': ReactionSerializer,
    }

    def get_serializer_class(self):  # pyright: ignore
        return self.serializer_mapping.get(self.action, self.serializer_class)

    def perform_destroy(self, instance):
        Comment.objects.soft_delete(instance)
        # perform cleanup
        Comment.objects.clean_up_soft_deleted()
