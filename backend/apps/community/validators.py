from django.core.validators import RegexValidator
from django.utils.deconstruct import deconstructible
from django.utils.translation import gettext_lazy as _


@deconstructible
class NameValidator(RegexValidator):
    regex = r'^[a-zA-Z0-9](?:[a-zA-Z0-9_-]*[a-zA-Z0-9])?$'
    message = _(
        "Community name may only contain letters, numbers, underscores, and hyphens, "
        "and cannot begin or end with a special character."
    )
    flags = 0
