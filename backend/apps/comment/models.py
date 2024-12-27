from django.contrib.postgres import indexes as idx
from django.db import models
from django.utils.translation import gettext_lazy as _
from django_ltree.models import TreeModel

from apps.user.models import Profile
from common.mixins.model_mixins import CreatedAtMixin

from .managers import CommentManager

# Create your models here.


class Comment(CreatedAtMixin, TreeModel):
    quibbler = models.ForeignKey(
        Profile, on_delete=models.SET_NULL, null=True, verbose_name=_('quibbler')
    )
    content = models.TextField(_('content'))
    upvotes = models.ManyToManyField(
        Profile, related_name='upvoted_comments', blank=True, verbose_name=_('upvotes')
    )
    downvotes = models.ManyToManyField(
        Profile,
        related_name='downvoted_comments',
        blank=True,
        verbose_name=_('downvotes'),
    )
    # flag
    deleted = models.BooleanField(default=False)
    # custom manager for soft-deletions handling
    objects = CommentManager()

    @property
    def children_count(self):
        return self.children().count()

    def __str__(self) -> str:
        return f"Comment by {self.quibbler}"

    class Meta:  # pyright: ignore
        indexes = [idx.GistIndex(fields=['path'])]
        verbose_name = 'Comment'
        verbose_name_plural = 'Comments'
