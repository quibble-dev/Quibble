from django.contrib.auth import authenticate
from drf_spectacular.utils import extend_schema
from rest_framework import exceptions, generics, permissions, views
from rest_framework.authtoken.models import Token
from rest_framework.response import Response

from common.api.exceptions import ServerError
from common.api.serializers import DetailResponseSerializer

from .serializers import (
    ProfileModelSerializer,
    UserAuthModelSerializer,
    UserAuthTokenSerializer,
)


class LoginAPIView(views.APIView):
    """
    Customized drf basic token authentication.

    This view authenticates the user using email and password credentials
    and issues a token upon successful login.
    """

    serializer_class = UserAuthModelSerializer

    @extend_schema(responses=UserAuthTokenSerializer)
    def post(self, request, format=None):
        user = authenticate(
            email=request.data.get('email'), password=request.data.get('password')
        )
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
            raise ServerError(f"An error occurred while logging out: {str(e)}")


class RegisterAPIView(generics.CreateAPIView):
    """
    View to handle registering of new users.
    """

    serializer_class = UserAuthModelSerializer


class MeAPIView(views.APIView):
    """
    View to retrieve information for the currently authenticated user.

    - `get`: Returns the details of the authenticated user based on their token.

    Permission:
    - Requires user authentication.
    """

    permission_classes = (permissions.IsAuthenticated,)
    serializer_class = ProfileModelSerializer

    def get(self, request):
        if request.user_profile:
            serializer = self.serializer_class(request.user_profile)
            return Response(serializer.data)
        else:
            raise exceptions.ValidationError('A valid profile must be provided.')
