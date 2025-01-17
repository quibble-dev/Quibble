from django.db import models
from django.utils.text import slugify
from django.utils.translation import gettext_lazy as _
from dynamic_filenames import FilePattern

from apps.comment.models import Comment
from apps.quiblet.models import Quiblet
from apps.user.models import Profile
from mixins.models.created_at import CreatedAtMixin
from mixins.models.is_public import IsPublicMixin
from mixins.models.shortuuid import ShortUUIDMixin

cover_file_pattern = FilePattern(filename_pattern="cover/{uuid:s}{ext}")

# Create your models here.


class Quib(CreatedAtMixin, IsPublicMixin, ShortUUIDMixin):
    quiblet = models.ForeignKey(
        Quiblet,
        related_name='quibs',
        verbose_name=_('quiblet'),
        on_delete=models.CASCADE,
    )
    quibber = models.ForeignKey(
        Profile,
        related_name='quibs',
        verbose_name=_('quibber'),
        on_delete=models.CASCADE,
    )
    highlighted = models.BooleanField(_('highlighted'), default=False)
    title = models.CharField(_('title'), max_length=255)
    slug = models.SlugField(_('slug'), max_length=25, blank=True)
    content = models.TextField(_('content'), blank=True)
    cover = models.ImageField(
        _('cover'),
        upload_to=cover_file_pattern,
        blank=True,
        null=True,
    )
    upvotes = models.ManyToManyField(
        Profile, related_name='upvoted_quibs', blank=True, verbose_name=_('upvotes')
    )
    downvotes = models.ManyToManyField(
        Profile,
        related_name='downvoted_quibs',
        blank=True,
        verbose_name=_('downvotes'),
    )
    comments = models.ManyToManyField(
        Comment, related_name='comments', blank=True, verbose_name=_('comments')
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
