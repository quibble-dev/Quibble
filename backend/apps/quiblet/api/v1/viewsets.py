from rest_framework.viewsets import ModelViewSet

from apps.quiblet.models import Quiblet

from .serializers import QuibletSerializer


class QuibletViewSet(ModelViewSet):
    queryset = Quiblet.objects.all()
    serializer_class = QuibletSerializer

    def perform_create(self, serializer):
        quibber = self.request.user_profile
        serializer.save(quibber=quibber)
