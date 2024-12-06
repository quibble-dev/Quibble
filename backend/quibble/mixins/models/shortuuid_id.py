from django.db import models
from django.utils.translation import gettext_lazy as _
from shortuuid.django_fields import ShortUUIDField


class ShortUUIDIdMixin(models.Model):
    """Adds an `id` field as primary key and a shortuuid generated one."""

    id = ShortUUIDField(  # type: ignore
        _('id'),
        editable=False,
        length=7,
        alphabet="abcdefghijklmnopqrstuvwxyz0123456789",
        primary_key=True,
    )

    class Meta:  # type: ignore
        abstract = True
