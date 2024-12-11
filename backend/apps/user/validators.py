from django.core.validators import RegexValidator
from django.utils.deconstruct import deconstructible
from django.utils.translation import gettext_lazy as _


@deconstructible
class UsernameValidator(RegexValidator):
    regex = r'^[a-zA-Z0-9](?:[a-zA-Z0-9_.]*[a-zA-Z0-9])?$'
    message = _(
        "Username must contain only letters, numbers, underscores, and periods, "
        "and cannot end with a special character."
    )
    flags = 0
