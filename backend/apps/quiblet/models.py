from django.db import models
from django.db.models import UniqueConstraint
from django.db.models.functions import Lower
from django.utils.translation import gettext_lazy as _
from dynamic_filenames import FilePattern

from apps.user.models import ProfileModel
from common.mixins.model_mixins import AvatarMixin, CreatedAtMixin, IsPublicMixin

cover_file_pattern = FilePattern(filename_pattern="cover/{uuid:s}{ext}")

# Create your models here.


class QuibletModel(AvatarMixin, CreatedAtMixin, IsPublicMixin):
    name = models.CharField(
        _('name'),
        unique=True,
        max_length=25,
        error_messages={'unique': 'Quiblet with this name already exists.'},
    )
    description = models.TextField(_('description'))
    cover = models.ImageField(
        _('cover'),
        upload_to=cover_file_pattern,
        blank=True,
        null=True,
    )
    members = models.ManyToManyField(
        ProfileModel, related_name='joined_quiblets', blank=True, verbose_name=_('members')
    )
    rangers = models.ManyToManyField(
        ProfileModel, related_name='ranged_quiblets', blank=True, verbose_name=_('rangers')
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
