from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response

from .serializers import ProfileSerializer, UserSerializer
from .models import Profile, User


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

    @action(detail=True)
    def profiles(self, request, pk=None):
        user = self.get_object()
        profiles = user.profiles.all()
        serializer = ProfileSerializer(profiles, many=True)

        return Response(serializer.data)


class ProfileViewSet(viewsets.ModelViewSet):
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer
