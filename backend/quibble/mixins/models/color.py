import random
from functools import partial

from django.db import models
from django.utils.translation import gettext_lazy as _


def get_random_color(choices):
    return random.choice([choice[0] for choice in choices])


class ColorMixin(models.Model):
    """Adds a `color` field with default selection."""

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
        _('color'),
        max_length=25,
        choices=COLOR_CHOICES,
        default=partial(get_random_color, COLOR_CHOICES),
    )

    class Meta:  # type: ignore
        abstract = True
