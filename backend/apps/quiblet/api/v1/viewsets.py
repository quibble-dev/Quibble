from http import HTTPMethod
from typing import cast

from django.db.models import QuerySet
from rest_framework import exceptions, response, viewsets
from rest_framework.decorators import action

from common.patches.request import PatchedHttpRequest

from ...models import QuibletModel
from .serializers import QuibletExistsSerializer, QuibletModelSerializer


class QuibletModelViewSet(viewsets.ModelViewSet):
    queryset = QuibletModel.objects.all()
    serializer_class = QuibletModelSerializer
    lookup_field = 'name'

    def get_queryset(self) -> QuerySet[QuibletModel]:  # pyright: ignore
        return super().get_queryset()

    def get_object(self) -> QuibletModel:  # pyright: ignore
        qs = self.get_queryset()
        filter_kwargs = {f'{self.lookup_field}__iexact': self.kwargs[self.lookup_field]}
        obj = qs.filter(**filter_kwargs).first()

        if not obj:
            raise exceptions.NotFound(
                f'Quiblet with name {self.kwargs[self.lookup_field]} not found.'
            )
        return obj

    def get_serializer_class(self):  # pyright: ignore
        if self.action == 'exists':
            return QuibletExistsSerializer
        return super().get_serializer_class()

    @action(detail=True, methods=[HTTPMethod.GET])
    def exists(self, request, name=None):
        res = dict(exists=False, name=name)

        quiblet = self.get_queryset().filter(name__iexact=name).first()
        if quiblet is not None:
            res['exists'] = True
            res['name'] = quiblet.name

        return response.Response(res)

    def perform_create(self, serializer):
        patched_request = cast(PatchedHttpRequest, self.request)

        quibbler = patched_request.user_profile

        quiblet = serializer.save()
        # add creator as member and ranger of the quiblet
        quiblet.members.add(quibbler)
        quiblet.rangers.add(quibbler)
