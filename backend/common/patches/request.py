from typing import Optional, Union

from django.contrib.auth.models import AnonymousUser
from django.http import HttpRequest

from apps.user.models import ProfileModel, User


class PatchedHttpRequest(HttpRequest):
    """
    Patched version of native HttpRequest with extra types.
    """

    user: Union[User, AnonymousUser]  # pyright: ignore
    user_profile: Optional[ProfileModel]
