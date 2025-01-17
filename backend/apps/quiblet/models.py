from django.db import models
from django.db.models import UniqueConstraint
from django.db.models.functions import Lower
from django.utils.translation import gettext_lazy as _
from dynamic_filenames import FilePattern

from apps.user.models import Profile
from mixins.models.avatar import AvatarMixin
from mixins.models.created_at import CreatedAtMixin
from mixins.models.is_public import IsPublicMixin

banner_file_pattern = FilePattern(filename_pattern="banner/{uuid:s}{ext}")

# Create your models here.


class Quiblet(AvatarMixin, CreatedAtMixin, IsPublicMixin):
    name = models.CharField(
        _('name'),
        unique=True,
        max_length=25,
        error_messages={'unique': 'Quiblet with this name already exists.'},
    )
    description = models.TextField(_('description'))
    title = models.CharField(_('title'), max_length=50, null=True, blank=True)
    banner = models.ImageField(
        _('banner'),
        upload_to=banner_file_pattern,
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
