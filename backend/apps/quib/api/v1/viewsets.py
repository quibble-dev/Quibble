from drf_spectacular.utils import extend_schema
from rest_framework import viewsets

from ...models import QuibModel
from .serializers import QuibSerializer, QuibSlimSerializer


@extend_schema(tags=['quibs & quiblets'])
class QuibViewSet(viewsets.ModelViewSet):
    queryset = QuibModel.objects.all()

    def get_serializer_class(self):  # pyright: ignore
        if self.action == 'list':
            return QuibSlimSerializer
        return QuibSerializer
