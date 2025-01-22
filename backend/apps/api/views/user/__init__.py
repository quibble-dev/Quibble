from rest_framework import exceptions, permissions, views
from rest_framework.response import Response

from ...serializers.user.profile import ProfileSerializer


class MeAPIView(views.APIView):
    """
    View to retrieve information for the currently authenticated user.

    - `get`: Returns the details of the authenticated user based on their token.

    Permission:
    - Requires user authentication.
    """

    permission_classes = (permissions.IsAuthenticated,)
    serializer_class = ProfileSerializer

    def get(self, request):
        if request.user_profile:
            serializer = self.serializer_class(request.user_profile, context={'request': request})
            return Response(serializer.data)
        else:
            raise exceptions.ValidationError('A valid profile must be provided.')
