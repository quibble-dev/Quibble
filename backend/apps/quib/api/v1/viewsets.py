from rest_framework import viewsets

from ...models import QuibModel
from .serializers import QuibSerializer, QuibSlimSerializer


class QuibViewSet(viewsets.ModelViewSet):
    queryset = QuibModel.objects.all()

    def get_serializer_class(self):  # pyright: ignore
        if self.action == 'list':
            return QuibSlimSerializer
        return QuibSerializer
