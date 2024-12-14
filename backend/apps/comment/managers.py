from django.db import models


class CommentManager(models.Manager):
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
        for comment_instance in self.filter(deleted=True):
            if comment_instance.children_count == 0:
                comment_instance.delete()
