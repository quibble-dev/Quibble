from django.db import models
from django.utils.text import slugify
from django.utils.translation import gettext_lazy as _

from apps.quiblet.models import Quiblet
from apps.user.models import Profile
from common.mixins import CreatedAtMixin, IsPublicMixin, ShortUUIDIdMixin


class Quib(CreatedAtMixin, IsPublicMixin, ShortUUIDIdMixin):
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
    likes = models.ManyToManyField(
        Profile, related_name='liked_quibs', blank=True, verbose_name=_('likes')
    )
    dislikes = models.ManyToManyField(
        Profile, related_name='disliked_quibs', blank=True, verbose_name=_('dislikes')
    )

    def save(self, *args, **kwargs):
        """Override save method to slugify title."""
        if not self.slug:
            self.slug = slugify(self.title[:25])

        super(Quib, self).save(*args, **kwargs)

    def __str__(self):
        return f'{self.pk}/{self.slug}'

    class Meta:  # type: ignore
        verbose_name = 'Quib'
        verbose_name_plural = 'Quibs'
        ordering = ['-created_at']
