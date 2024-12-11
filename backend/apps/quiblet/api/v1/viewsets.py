from typing import cast

from drf_spectacular.utils import extend_schema
from rest_framework.viewsets import ModelViewSet

from common.patches.request import PatchedHttpRequest

from ...models import Quib, Quiblet
from .serializers import QuibletSerializer, QuibSerializer


@extend_schema(tags=['quibs & quiblets'])
class QuibletViewSet(ModelViewSet):
    queryset = Quiblet.objects.all()
    serializer_class = QuibletSerializer

    def perform_create(self, serializer):
        patched_request = cast(PatchedHttpRequest, self.request)

        quibbler = patched_request.user_profile

        quiblet = serializer.save()
        # add creator as member and ranger of the quiblet
        quiblet.members.add(quibbler)
        quiblet.rangers.add(quibbler)


@extend_schema(tags=['quibs & quiblets'])
class QuibViewSet(ModelViewSet):
    queryset = Quib.objects.all()
    serializer_class = QuibSerializer
