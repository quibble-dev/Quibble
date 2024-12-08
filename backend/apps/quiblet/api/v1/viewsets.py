from rest_framework.viewsets import ModelViewSet

from apps.quiblet.models import Quiblet

from .serializers import QuibletSerializer


class QuibletViewSet(ModelViewSet):
    queryset = Quiblet.objects.all()
    serializer_class = QuibletSerializer

    def perform_create(self, serializer):
        quibbler = self.request.user_profile  # type: ignore

        quiblet = serializer.save()

        quiblet.members.add(quibbler)
        quiblet.rangers.add(quibbler)
