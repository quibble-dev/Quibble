from drf_spectacular.utils import extend_schema
from rest_framework.viewsets import ModelViewSet

from ...models import Quib, Quiblet
from .serializers import QuibletSerializer, QuibSerializer


@extend_schema(tags=['quibs & quiblets'])
class QuibletViewSet(ModelViewSet):
    queryset = Quiblet.objects.all()
    serializer_class = QuibletSerializer

    def perform_create(self, serializer):
        quibbler = self.request.user_profile  # type: ignore

        quiblet = serializer.save()

        quiblet.members.add(quibbler)
        quiblet.rangers.add(quibbler)


@extend_schema(tags=['quibs & quiblets'])
class QuibViewSet(ModelViewSet):
    queryset = Quib.objects.all()
    serializer_class = QuibSerializer
