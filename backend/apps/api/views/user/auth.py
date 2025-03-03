from django.conf import settings
from django.contrib.auth import authenticate
from django.utils import timezone
from drf_spectacular.utils import extend_schema
from rest_framework import exceptions, generics, permissions, views
from rest_framework.authtoken.models import Token
from rest_framework.response import Response

from apps.user.models import Profile

from ...bases.serializers import DetailResponseSerializer
from ...exceptions import ServerError
from ...serializers.user.auth import AuthSerializer, AuthTokenSerializer


class ProfileSelectAPIView(views.APIView):
    """API View to select profile which sets cookie to response"""

    # authentication_classes = []

    def post(self, request, profile_id=None):
        profile = generics.get_object_or_404(Profile, id=profile_id, user=request.user)

        response = Response({})
        response.set_cookie(
            'profile-id',
            value=str(profile.pk),
            expires=timezone.now() + timezone.timedelta(days=7),
            httponly=True,
            secure=False if settings.DEBUG else True,
            samesite='Lax',
        )

        return response


class LoginAPIView(views.APIView):
    """
    Customized drf basic token authentication.

    This view authenticates the user using email and password credentials
    and issues a token upon successful login.
    """

    serializer_class = AuthSerializer

    @extend_schema(responses=AuthTokenSerializer)
    def post(self, request, format=None):
        user = authenticate(email=request.data.get('email'), password=request.data.get('password'))
        if user:
            token, _ = Token.objects.get_or_create(user=user)
            return Response({'token': token.key})
        else:
            raise exceptions.AuthenticationFailed()


class LogoutAPIView(views.APIView):
    """
    View to handle user logout by deleting the authentication token.
    """

    permission_classes = (permissions.IsAuthenticated,)

    @extend_schema(request=None, responses=DetailResponseSerializer)
    def post(self, request, format=None):
        try:
            Token.objects.filter(user=request.user).delete()
            return Response({'detail': 'Successfully logged out.'})

        except Exception as e:
            raise ServerError(f'An error occurred while logging out: {str(e)}')


class RegisterAPIView(generics.CreateAPIView):
    """
    View to handle registering of new users.
    """

    serializer_class = AuthSerializer
