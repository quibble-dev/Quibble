from django.db import models
from django.utils.text import slugify
from django.utils.translation import gettext_lazy as _
from dynamic_filenames import FilePattern

from apps.comment.models import CommentModel
from apps.quiblet.models import QuibletModel
from apps.user.models import ProfileModel
from common.mixins.model_mixins import CreatedAtMixin, IsPublicMixin, ShortUUIDMixin

cover_file_pattern = FilePattern(filename_pattern="cover/{uuid:s}{ext}")

# Create your models here.


class QuibModel(CreatedAtMixin, IsPublicMixin, ShortUUIDMixin):
    quiblet = models.ForeignKey(
        QuibletModel,
        related_name='quibs',
        verbose_name=_('quiblet'),
        on_delete=models.CASCADE,
    )
    quibber = models.ForeignKey(
        ProfileModel,
        related_name='quibs',
        verbose_name=_('quibber'),
        on_delete=models.CASCADE,
    )
    title = models.CharField(_('title'), max_length=255)
    slug = models.SlugField(_('slug'), editable=False, max_length=25, blank=True)
    content = models.TextField(_('content'), blank=True)
    cover = models.ImageField(
        _('cover'),
        upload_to=cover_file_pattern,
        blank=True,
        null=True,
    )
    upvotes = models.ManyToManyField(
        ProfileModel, related_name='upvoted_quibs', blank=True, verbose_name=_('upvotes')
    )
    downvotes = models.ManyToManyField(
        ProfileModel,
        related_name='downvoted_quibs',
        blank=True,
        verbose_name=_('downvotes'),
    )
    comments = models.ManyToManyField(
        CommentModel, related_name='comments', blank=True, verbose_name=_('comments')
    )

    def save(self, *args, **kwargs):
        """Override save method to slugify title."""
        if not self.slug:
            self.slug = slugify(self.title[:25])

        super().save(*args, **kwargs)

    def __str__(self) -> str:
        return f'{self.pk}/{self.slug}'

    class Meta:  # pyright: ignore
        verbose_name = 'Quib'
        verbose_name_plural = 'Quibs'
        ordering = ['-created_at']
