from http import HTTPMethod
from typing import cast

from django.db.models import QuerySet
from drf_spectacular.utils import extend_schema
from rest_framework import exceptions, response, viewsets
from rest_framework.decorators import action

from apps.quiblet.models import Quiblet

from ...http import HttpRequest
from ...serializers.community import (
    QuibletDetailedSerializer,
    QuibletExistsSerializer,
    QuibletSerializer,
)
from ...serializers.post import QuibSerializer
from ...serializers.post.highlighted import QuibHighlightedSerializer


class QuibletViewSet(viewsets.ModelViewSet):
    queryset = Quiblet.objects.all()
    # default serializer
    serializer_class = QuibletSerializer
    lookup_field = 'name'

    # extra custom serializers
    serializer_classes = {
        'retrieve': QuibletDetailedSerializer,
        # extra actions
        'exists': QuibletExistsSerializer,
        'quibs': QuibSerializer,
        'highlighted_quibs': QuibHighlightedSerializer,
    }

    def get_queryset(self) -> QuerySet[Quiblet]:  # pyright: ignore
        return super().get_queryset()

    def get_object(self) -> Quiblet:  # pyright: ignore
        qs = self.get_queryset()
        filter_kwargs = {f'{self.lookup_field}__iexact': self.kwargs[self.lookup_field]}
        obj = qs.filter(**filter_kwargs).first()

        if not obj:
            raise exceptions.NotFound(
                f'Quiblet with name <b>{self.kwargs[self.lookup_field]}</b> not found.'
            )
        return obj

    def get_serializer_class(self):  # pyright: ignore
        if self.action in self.serializer_classes:
            return self.serializer_classes[self.action]
        return self.serializer_class

    @action(detail=True, methods=[HTTPMethod.GET])
    def exists(self, request, name=None):
        res = dict(exists=False, name=name)

        quiblet = self.get_queryset().filter(name__iexact=name).first()
        if quiblet is not None:
            res['exists'] = True
            res['name'] = quiblet.name

        return response.Response(res)

    @extend_schema(responses=QuibSerializer(many=True))
    @action(detail=True, methods=[HTTPMethod.GET])
    def quibs(self, request, name=None):
        quibs = self.get_object().quibs.all()  # pyright: ignore
        serializer = QuibSerializer(quibs, many=True, context={'request': request})

        return response.Response(serializer.data)

    @extend_schema(responses=QuibHighlightedSerializer(many=True))
    @action(detail=True, methods=[HTTPMethod.GET])
    def highlighted_quibs(self, request, name=None):
        quibs = self.get_object().quibs.filter(highlighted=True)  # pyright: ignore
        serializer = QuibHighlightedSerializer(
            quibs, many=True, context={'request': request}
        )

        return response.Response(serializer.data)

    def perform_create(self, serializer):
        patched_request = cast(HttpRequest, self.request)

        quibbler = patched_request.user_profile

        quiblet = serializer.save()
        # add creator as member and ranger of the quiblet
        quiblet.members.add(quibbler)
        quiblet.rangers.add(quibbler)
