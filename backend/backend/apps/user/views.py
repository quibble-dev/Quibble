from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response

from .serializers import ProfileSerializer, UserSerializer
from .models import Profile, User


class UserViewSet(viewsets.ModelViewSet):
    """
    CRUD operations for User model
    """

    queryset = User.objects.all()
    serializer_class = UserSerializer

    @action(detail=True)
    def profiles(self, request, pk=None):
        """
        Show all profiles associated with specific user
        """

        user = self.get_object()
        user_profiles = user.profiles.all()
        serializer = ProfileSerializer(user_profiles, many=True)

        return Response(serializer.data)


class ProfileViewSet(viewsets.ModelViewSet):
    """
    CRUD operations for Profile model
    """

    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer
