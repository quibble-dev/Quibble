from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from django.db import models
from django.utils.translation import gettext_lazy as _
from dynamic_filenames import FilePattern

from django_core.mixins.models.color import ColorMixin
from django_core.mixins.models.created_at import CreatedAtMixin

from .managers import CustomUserManager

# dynamic avatar filename
profile_avatar_pattern = FilePattern(filename_pattern="avatar/{uuid:s}{ext}")


class User(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(_('email address'), unique=True)
    date_joined = models.DateTimeField(_('date joined'), auto_now_add=True)
    is_staff = models.BooleanField(
        _("staff status"),
        default=False,
        help_text=_("Designates whether the user can log into this admin site."),
    )
    is_active = models.BooleanField(
        _("active"),
        default=True,
        help_text=_(
            "Designates whether this user should be treated as active. "
            "Unselect this instead of deleting accounts."
        ),
    )

    objects = CustomUserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []


class Profile(CreatedAtMixin, ColorMixin):
    user = models.ForeignKey(User, related_name='profiles', on_delete=models.CASCADE)
    username = models.CharField(_('username'), unique=True, max_length=25)
    avatar = models.ImageField(
        _('avatar'),
        upload_to=profile_avatar_pattern,
        blank=True,
        null=True,
    )
    first_name = models.CharField(_('first name'), max_length=255, blank=True, null=True)
    last_name = models.CharField(_('last name'), max_length=255, blank=True, null=True)

    def __str__(self):
        return f"u/{self.username}"
