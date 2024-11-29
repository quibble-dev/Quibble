from django.db import models
from django.utils.translation import gettext_lazy as _


class CreatedAtMixin(models.Model):
    """Adds `created_at` auto added date field"""

    created_at = models.DateTimeField(_('create at'), auto_now_add=True)

    class Meta:
        abstract = True


class ColorMixin(models.Model):
    class Colors(models.TextChoices):
        PRIMARY = 'primary', _('primary')
        SECONDARY = 'secondary', _('secondary')
        ACCENT = 'accent', _('accent')
        NEUTRAL = 'neutral', _('neutral')
        INFO = 'info', _('info')
        SUCCESS = 'success', _('success')
        WARNING = 'warning', _('warning')
        ERROR = 'error', _('error')

    color = models.CharField(max_length=25, choices=Colors.choices, null=True, blank=True)

    class Meta:
        abstract = True
