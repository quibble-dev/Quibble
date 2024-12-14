from django.db import models

from .models import CommentModel


class CommentManager(models.Manager):
    def soft_delete(self, instance: CommentModel):
        # if no children- hard delete
        if instance.children_count == 0:
            instance.delete()
        # else- soft delete
        else:
            instance.deleted = True
            instance.content = "[deleted]"
            instance.save()

    def clean_up_soft_deleted(self):
        self.filter(deleted=True, children_count=0).delete()
