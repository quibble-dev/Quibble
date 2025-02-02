from django.contrib.auth import authenticate
from drf_spectacular.utils import extend_schema
from rest_framework import exceptions, generics, permissions, views
from rest_framework.authtoken.models import Token
from rest_framework.response import Response

from ...bases.serializers import DetailResponseSerializer
from ...exceptions import ServerError
from ...serializers.user.auth import AuthSerializer, AuthTokenSerializer


@extend_schema(tags=['auth'])
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


@extend_schema(tags=['auth'])
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
            raise ServerError(f"An error occurred while logging out: {str(e)}")


@extend_schema(tags=['auth'])
class RegisterAPIView(generics.CreateAPIView):
    """
    View to handle registering of new users.
    """

    serializer_class = AuthSerializer
