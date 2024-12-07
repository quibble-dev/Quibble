from django.db import models
from django.db.models import UniqueConstraint
from django.db.models.functions import Lower
from django.utils.text import slugify
from django.utils.translation import gettext_lazy as _
from dynamic_filenames import FilePattern

from apps.user.models import Profile
from common.mixins import AvatarMixin, CreatedAtMixin, IsPublicMixin, ShortUUIDIdMixin


class Quiblet(AvatarMixin, CreatedAtMixin, IsPublicMixin, ShortUUIDIdMixin):
    name = models.CharField(_('name'), unique=True, max_length=25)
    description = models.TextField(_('description'))
    cover = models.ImageField(
        _('cover'),
        upload_to=FilePattern(filename_pattern="cover/{uuid:s}{ext}"),
        blank=True,
        null=True,
    )
    members = models.ManyToManyField(
        Profile, related_name='joined_quiblets', blank=True, verbose_name=_('members')
    )
    rangers = models.ManyToManyField(
        Profile, related_name='ranged_quiblets', blank=True, verbose_name=_('rangers')
    )

    class Meta:  # type: ignore
        verbose_name = 'Quiblet'
        verbose_name_plural = 'Quiblets'
        ordering = ['-created_at']
        constraints = [
            UniqueConstraint(Lower('name'), name='unique_quiblet_name_case_insensitive')
        ]

    def __str__(self):
        return f'q/{self.name}'
