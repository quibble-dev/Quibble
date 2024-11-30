import random
from functools import partial

from django.db import models
from django.utils.translation import gettext_lazy as _


class CreatedAtMixin(models.Model):
    """Adds `created_at` auto added date field"""

    created_at = models.DateTimeField(_('create at'), auto_now_add=True)

    class Meta:
        abstract = True


def get_random_color(choices):
    return random.choice([choice[0] for choice in choices])


class ColorMixin(models.Model):
    COLOR_CHOICES = [
        ('primary', 'primary'),
        ('secondary', 'secondary'),
        ('accent', 'accent'),
        ('neutral', 'neutral'),
        ('info', 'info'),
        ('success', 'success'),
        ('warning', 'warning'),
        ('error', 'error'),
    ]

    color = models.CharField(
        max_length=25,
        choices=COLOR_CHOICES,
        default=partial(get_random_color, COLOR_CHOICES),
    )

    class Meta:
        abstract = True
