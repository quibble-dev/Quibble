from django.db import models
from django.utils.translation import gettext_lazy as _
from dynamic_filenames import FilePattern

# dynamic avatar filename
quiblet_avatar_pattern = FilePattern(filename_pattern="avatar/{uuid:s}{ext}")
quiblet_cover_pattern = FilePattern(filename_pattern="cover/{uuid:s}{ext}")


class Quiblets(models.Model):
    name = models.CharField(_('name'), unique=True, max_length=25)
    description = models.TextField(_('description'))
    avatar = models.ImageField(
        _('avatar'),
        upload_to=quiblet_avatar_pattern,
        blank=True,
        null=True,
    )
    cover = models.ImageField(
        _('cover'),
        upload_to=quiblet_cover_pattern,
        blank=True,
        null=True,
    )
