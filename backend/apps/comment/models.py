from django.contrib.postgres import indexes as idx
from django.db import models
from django.utils.translation import gettext_lazy as _
from django_ltree.models import TreeModel

from apps.user.models import ProfileModel
from common.mixins.model_mixins import CreatedAtMixin

# Create your models here.


class CommentModel(CreatedAtMixin, TreeModel):
    quibbler = models.ForeignKey(
        ProfileModel, on_delete=models.CASCADE, verbose_name=_('quibbler')
    )
    content = models.TextField(_('content'))
    upvotes = models.ManyToManyField(
        ProfileModel, related_name='upvotes', blank=True, verbose_name=_('upvotes')
    )
    downvotes = models.ManyToManyField(
        ProfileModel, related_name='downvotes', blank=True, verbose_name=_('downvotes')
    )

    @property
    def children_count(self):
        return self.children().count()

    def __str__(self) -> str:
        return f"Comment by {self.quibbler.username}"

    class Meta:  # pyright: ignore
        indexes = [idx.GistIndex(fields=['path'])]
        verbose_name = 'Comment'
        verbose_name_plural = 'Comments'
