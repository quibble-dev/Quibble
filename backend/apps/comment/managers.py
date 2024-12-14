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
