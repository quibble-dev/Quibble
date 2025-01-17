from django.db import models
from django.utils.translation import gettext_lazy as _


class CreatedAtMixin(models.Model):
    """Adds `created_at` auto added date field."""

    created_at = models.DateTimeField(_('create at'), auto_now_add=True)

    class Meta:  # pyright: ignore
        abstract = True
