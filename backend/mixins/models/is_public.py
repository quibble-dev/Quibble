from django.db import models
from django.utils.translation import gettext_lazy as _


class IsPublicMixin(models.Model):
    """Adds a `is_public` boolean field"""

    is_public = models.BooleanField(_('Is public'), default=True)

    class Meta:  # pyright: ignore
        abstract = True
