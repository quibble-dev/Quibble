from django.contrib.auth import authenticate
from rest_framework import permissions, views, exceptions
from rest_framework.authtoken.models import Token
from rest_framework.response import Response

from core.exceptions import ServerError
from .serializers import UserSerializer


class LoginAPIView(views.APIView):
    """
    Customized drf basic token authentication.

    This view authenticates the user using email and password credentials
    and issues a token upon successful login.
    """

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
        serializer = UserSerializer(request.user)
        return Response(serializer.data)
