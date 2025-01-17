from http import HTTPMethod
from typing import cast

from django.db.models import QuerySet
from drf_spectacular.utils import extend_schema
from rest_framework import exceptions, response, viewsets
from rest_framework.decorators import action

from apps.community.models import Community

from ...http import HttpRequest
from ...serializers.community import (
    CommunityDetailedSerializer,
    CommunityExistsSerializer,
    CommunitySerializer,
)
from ...serializers.post import PostSerializer
from ...serializers.post.highlighted import PostHighlightedSerializer


class CommunityViewSet(viewsets.ModelViewSet):
    queryset = Community.objects.all()
    # default serializer
    serializer_class = CommunitySerializer
    lookup_field = 'name'

    # extra custom serializers
    serializer_classes = {
        'retrieve': CommunityDetailedSerializer,
        # extra actions
        'exists': CommunityExistsSerializer,
        'posts': PostSerializer,
        'highlighted_posts': PostHighlightedSerializer,
    }

    def get_queryset(self) -> QuerySet[Community]:  # pyright: ignore
        return super().get_queryset()

    def get_object(self) -> Community:  # pyright: ignore
        qs = self.get_queryset()
        filter_kwargs = {f'{self.lookup_field}__iexact': self.kwargs[self.lookup_field]}
        obj = qs.filter(**filter_kwargs).first()

        if not obj:
            raise exceptions.NotFound(
                f'Community with name <b>{self.kwargs[self.lookup_field]}</b> not found.'
            )
        return obj

    def get_serializer_class(self):  # pyright: ignore
        if self.action in self.serializer_classes:
            return self.serializer_classes[self.action]
        return self.serializer_class

    @action(detail=True, methods=[HTTPMethod.GET])
    def exists(self, request, name=None):
        res = dict(exists=False, name=name)

        community = self.get_queryset().filter(name__iexact=name).first()
        if community is not None:
            res['exists'] = True
            res['name'] = community.name

        return response.Response(res)

    @extend_schema(responses=PostSerializer(many=True))
    @action(detail=True, methods=[HTTPMethod.GET])
    def posts(self, request, name=None):
        posts = self.get_object().posts.all()  # pyright: ignore
        serializer = PostSerializer(posts, many=True, context={'request': request})

        return response.Response(serializer.data)

    @extend_schema(responses=PostHighlightedSerializer(many=True))
    @action(detail=True, methods=[HTTPMethod.GET])
    def highlighted_posts(self, request, name=None):
        posts = self.get_object().posts.filter(highlighted=True)  # pyright: ignore
        serializer = PostHighlightedSerializer(
            posts, many=True, context={'request': request}
        )

        return response.Response(serializer.data)

    def perform_create(self, serializer):
        patched_request = cast(HttpRequest, self.request)

        creator = patched_request.user_profile
        # add creator as member and ranger of the community
        community = serializer.save()
        community.members.add(creator)
        community.rangers.add(creator)
