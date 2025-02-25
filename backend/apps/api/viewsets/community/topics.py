from drf_spectacular.utils import extend_schema
from rest_framework import viewsets

from apps.community.models import Topic

from ...serializers.community.topics import TopicSerializer


@extend_schema(tags=['communities & topics'])
class TopicViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Topic.objects.filter(parent__isnull=True)
    serializer_class = TopicSerializer
