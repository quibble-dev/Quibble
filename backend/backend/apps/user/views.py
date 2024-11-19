from django.contrib.auth import authenticate
from rest_framework import permissions, views, exceptions
from rest_framework.authtoken.models import Token
from rest_framework.response import Response

from drf_spectacular.utils import extend_schema
from drf_standardized_errors.openapi_serializers import ErrorResponse401Serializer

from core.exceptions import ServerError
from .serializers import ProfileSerializer, AuthSerializer, AuthTokenResponseSerializer


class LoginAPIView(views.APIView):
    """
    Customized drf basic token authentication.

    This view authenticates the user using email and password credentials
    and issues a token upon successful login.
    """

    serializer_class = AuthSerializer

    @extend_schema(
        responses={
            200: AuthTokenResponseSerializer,
            401: ErrorResponse401Serializer,
        }
    )
    def post(self, request, format=None):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
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

    def post(self, request, format=None):
        try:
            Token.objects.filter(user=request.user).delete()
            return Response({'detail': 'Successfully logged out.'})

        except Exception as e:
            raise ServerError(f"An error occurred while logging out: {str(e)}")


class MeAPIView(views.APIView):
    """
    View to retrieve information for the currently authenticated user.

    - `get`: Returns the details of the authenticated user based on their token.

    Permission:
    - Requires user authentication.
    """

    permission_classes = (permissions.IsAuthenticated,)

    def get(self, request):
        if request.user_profile:
            serializer = ProfileSerializer(request.user_profile)
            return Response(serializer.data)
        else:
            raise exceptions.ValidationError('A valid profile must be provided.')
