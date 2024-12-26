from django.db import models
from django.utils.translation import gettext_lazy as _
from dynamic_filenames import FilePattern
from shortuuid.django_fields import ShortUUIDField


class CreatedAtMixin(models.Model):
    """Adds `created_at` auto added date field."""

    created_at = models.DateTimeField(_('create at'), auto_now_add=True)

    class Meta:  # pyright: ignore
        abstract = True


class AvatarMixin(models.Model):
    """Adds an `avatar` field with file upload pattern."""

    avatar = models.ImageField(
        _('avatar'),
        upload_to=FilePattern(filename_pattern="avatar/{uuid:s}{ext}"),
        blank=True,
        null=True,
    )

    class Meta:  # pyright: ignore
        abstract = True


class IsPublicMixin(models.Model):
    """Adds a `is_public` boolean field"""

    is_public = models.BooleanField(_('is public'), default=True)

    class Meta:  # pyright: ignore
        abstract = True


class ShortUUIDMixin(models.Model):
    """Adds an `id` field as primary key and a shortuuid generated one."""

    id = ShortUUIDField(  # pyright: ignore
        _('id'),
        editable=False,
        length=7,
        alphabet="abcdefghijklmnopqrstuvwxyz0123456789",
        primary_key=True,
    )

    class Meta:  # pyright: ignore
        abstract = True


class RatioMixin(models.Model):
    @property
    def ratio(self):
        return self.upvotes.count() - self.downvotes.count()  # type: ignore

    class Meta:
        abstract = True
