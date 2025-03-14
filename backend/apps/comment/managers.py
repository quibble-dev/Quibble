from django.db.models import Count, F
from django_ltree.managers import TreeManager


class CommentManager(TreeManager):
    def soft_delete(self, instance):
        # if no children- hard delete
        if instance.children_count == 0:
            instance.delete()
        # else- soft delete
        else:
            instance.deleted = True
            instance.content = "[deleted]"
            instance.quibbler = None
            instance.save()

    def clean_up_soft_deleted(self):
        # cleanup all comment instances with no children
        for comment in self.filter(deleted=True):
            if comment.children_count == 0:
                comment.delete()

    def with_ratio(self):
        # returns annotated ratio property
        return self.annotate(
            upvote_count=Count('upvotes'),
            downvote_count=Count('downvotes'),
            ratio=F('upvote_count') - F('downvote_count'),
        )
