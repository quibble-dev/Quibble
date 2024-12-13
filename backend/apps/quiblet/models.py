from django.db import models
from django.db.models import UniqueConstraint
from django.db.models.functions import Lower
from django.utils.text import slugify
from django.utils.translation import gettext_lazy as _
from dynamic_filenames import FilePattern

from apps.comment.models import Comment
from apps.user.models import Profile
from common.mixins.model_mixins import (
    AvatarMixin,
    CreatedAtMixin,
    IsPublicMixin,
    ShortUUIDMixin,
)

cover_file_pattern = FilePattern(filename_pattern="cover/{uuid:s}{ext}")

# models


class Quiblet(AvatarMixin, CreatedAtMixin, IsPublicMixin):
    name = models.CharField(_('name'), unique=True, max_length=25)
    description = models.TextField(_('description'))
    cover = models.ImageField(
        _('cover'),
        upload_to=cover_file_pattern,
        blank=True,
        null=True,
    )
    members = models.ManyToManyField(
        Profile, related_name='joined_quiblets', blank=True, verbose_name=_('members')
    )
    rangers = models.ManyToManyField(
        Profile, related_name='ranged_quiblets', blank=True, verbose_name=_('rangers')
    )

    def __str__(self) -> str:
        return f'q/{self.name}'

    class Meta:  # pyright: ignore
        verbose_name = 'Quiblet'
        verbose_name_plural = 'Quiblets'
        ordering = ['-created_at']
        constraints = [
            UniqueConstraint(Lower('name'), name='unique_quiblet_name_case_insensitive')
        ]


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
    title = models.CharField(_('title'), max_length=255)
    slug = models.SlugField(_('slug'), editable=False, max_length=25, blank=True)
    content = models.TextField(_('content'))
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
        Profile, related_name='downvoted_quibs', blank=True, verbose_name=_('downvotes')
    )
    comments = models.ManyToManyField(
        Comment, related_name='comments', blank=True, verbose_name=_('comments')
    )

    def save(self, *args, **kwargs):
        """Override save method to slugify title."""
        if not self.slug:
            self.slug = slugify(self.title[:25])

        super(Quib, self).save(*args, **kwargs)

    def __str__(self) -> str:
        return f'{self.pk}/{self.slug}'

    class Meta:  # pyright: ignore
        verbose_name = 'Quib'
        verbose_name_plural = 'Quibs'
        ordering = ['-created_at']
