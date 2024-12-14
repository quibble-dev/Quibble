from typing import cast

from rest_framework.viewsets import ModelViewSet

from common.patches.request import PatchedHttpRequest

from ...models import QuibletModel
from .serializers import QuibletSerializer


class QuibletModelViewSet(ModelViewSet):
    queryset = QuibletModel.objects.all()
    serializer_class = QuibletSerializer

    def perform_create(self, serializer):
        patched_request = cast(PatchedHttpRequest, self.request)

        quibbler = patched_request.user_profile

        quiblet = serializer.save()
        # add creator as member and ranger of the quiblet
        quiblet.members.add(quibbler)
        quiblet.rangers.add(quibbler)
