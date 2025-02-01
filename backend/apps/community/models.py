from django.db import models
from django.db.models import UniqueConstraint
from django.db.models.functions import Lower
from django.utils.translation import gettext_lazy as _
from dynamic_filenames import FilePattern

from apps.user.models import Profile
from mixins.models.avatar import AvatarMixin
from mixins.models.created_at import CreatedAtMixin
from mixins.models.is_public import IsPublicMixin

# Create your models here.


class Community(AvatarMixin, CreatedAtMixin, IsPublicMixin):
    name = models.CharField(
        _('Name'),
        unique=True,
        max_length=25,
        error_messages={'unique': 'Community with this name already exists.'},
    )
    description = models.TextField(_('Description'))
    title = models.CharField(_('Title'), max_length=50, null=True, blank=True)
    banner = models.ImageField(
        _('Banner'),
        upload_to=FilePattern(filename_pattern="community_banner/{uuid:s}{ext}"),
        blank=True,
        null=True,
    )
    members = models.ManyToManyField(
        Profile, related_name='joined_communities', blank=True, verbose_name=_('Members')
    )
    moderators = models.ManyToManyField(
        Profile,
        related_name='moderated_communities',
        blank=True,
        verbose_name=_('Moderators'),
    )
    rangers = models.ManyToManyField(
        Profile,
        related_name='ranged_communities',
        blank=True,
        verbose_name=_('Rangers'),
    )

    def __str__(self) -> str:
        return f'q/{self.name}'

    class Meta:  # pyright: ignore
        verbose_name = _('Community')
        verbose_name_plural = _('Communities')
        ordering = ['-created_at']
        constraints = [
            UniqueConstraint(Lower('name'), name='unique_community_name_case_insensitive')
        ]
