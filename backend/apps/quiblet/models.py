from django.db import models
from django.utils.translation import gettext_lazy as _
from dynamic_filenames import FilePattern

from apps.user.models import Profile
from shared.mixins.model_mixins import AvatarMixin, CreatedAtMixin


class Quiblet(AvatarMixin, CreatedAtMixin):
    name = models.CharField(_('name'), unique=True, max_length=25)
    description = models.TextField(_('description'))
    cover = models.ImageField(
        _('cover'),
        upload_to=FilePattern(filename_pattern="cover/{uuid:s}{ext}"),
        blank=True,
        null=True,
    )
    is_public = models.BooleanField(_('is public'), default=True)
    members = models.ManyToManyField(
        Profile, related_name='quiblets', blank=True, verbose_name=_('members')
    )
    rangers = models.ManyToManyField(
        Profile, related_name='ranged_quiblets', blank=True, verbose_name=_('rangers')
    )

    class Meta:
        verbose_name = 'Quiblet'
        verbose_name_plural = 'Quiblets'
        ordering = ['-created_at']

    def __str__(self):
        return self.name
