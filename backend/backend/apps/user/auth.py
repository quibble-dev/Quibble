from knox.auth import TokenAuthentication

from .models import Profile


class ExtendedTokenAuthentication(TokenAuthentication):
    """
    Extended knox TokenAuthentication
    which includes 'user_profile' field on request
    """

    def authenticate(self, request):
        user_auth_tuple = super().authenticate(request)
        if not user_auth_tuple:
            return None

        user, _ = user_auth_tuple

        profile_id = request.headers.get('Profile-ID')
        if profile_id:
            request.user_profile = Profile.objects.filter(id=profile_id, user=user).first()

        return user_auth_tuple
