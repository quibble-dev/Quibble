from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils.translation import gettext_lazy as _

from common.mixins import AvatarMixin, ColorMixin


class CustomUser(AbstractUser, ColorMixin, AvatarMixin):
    email = models.EmailField(
        _("Email address"),
        unique=True,
        error_messages={'unique': _('A user with that email already exists.')},
    )
    bio = models.TextField(_('Bio'))

    def __str__(self):
        return f"u/{self.username}"

    class Meta:  # type: ignore
        ordering = ['-date_joined']
