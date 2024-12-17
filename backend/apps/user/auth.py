from rest_framework import exceptions
from rest_framework.authentication import TokenAuthentication

from .models import Profile


class ExtendedTokenAuthentication(TokenAuthentication):
    """
    Extended drf TokenAuthentication
    which includes 'user_profile' field on request
    """

    keyword = 'Bearer'

    def authenticate(self, request):
        user_auth_token_tuple = super().authenticate(request)
        if not user_auth_token_tuple:
            return None

        user, auth_token = user_auth_token_tuple

        profile_id = request.headers.get('Profile-Id')
        user_profile = None

        if profile_id:
            try:
                user_profile = Profile.objects.get(id=profile_id, user=user)
            except Profile.DoesNotExist:
                raise exceptions.PermissionDenied(
                    'Profile does not exist or does not belong to the authenticated user.'
                )

        request.user_profile = user_profile

        return (user, auth_token)
