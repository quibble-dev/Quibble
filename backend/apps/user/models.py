from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from django.db import models
from django.utils.translation import gettext_lazy as _

from common.mixins.model_mixins import AvatarMixin, ColorMixin, CreatedAtMixin

from .managers import CustomUserManager
from .validators import UsernameValidator


class User(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(_('email address'), unique=True)
    date_joined = models.DateTimeField(_('date joined'), auto_now_add=True)
    is_staff = models.BooleanField(
        _("staff status"),
        default=False,
        help_text=_("designates whether the user can log into this admin site."),
    )
    is_active = models.BooleanField(
        _("active"),
        default=True,
        help_text=_(
            "designates whether this user should be treated as active. unselect this instead of deleting accounts."
        ),
    )

    objects = CustomUserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    class Meta:  # pyright: ignore
        verbose_name = 'User'
        verbose_name_plural = 'Users'
        ordering = ['-date_joined']


class ProfileModel(CreatedAtMixin, ColorMixin, AvatarMixin):
    username_validator = UsernameValidator()

    user = models.ForeignKey(User, related_name='profiles', on_delete=models.CASCADE)
    username = models.CharField(
        _('username'),
        unique=True,
        max_length=25,
        validators=[username_validator],
        help_text=_("Required. 25 characters or fewer. Letters, digits and ./_ only."),
        error_messages={
            "unique": _("A profile with that username already exists."),
        },
    )
    first_name = models.CharField(_('first name'), max_length=255, blank=True, null=True)
    last_name = models.CharField(_('last name'), max_length=255, blank=True, null=True)
    bio = models.TextField(_('Bio'), blank=True, null=True)

    def __str__(self):
        return f"u/{self.username}"

    class Meta:  # pyright: ignore
        verbose_name = 'Profile'
        verbose_name_plural = 'Profiles'
        ordering = ['-created_at']
