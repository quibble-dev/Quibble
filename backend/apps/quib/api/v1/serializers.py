from rest_framework import serializers

from apps.quiblet.api.v1.serializers import QuibletBasicSerializer
from apps.user.api.v1.serializers import ProfileBasicSerializer

from ...models import Quib


class QuibSerializer(serializers.ModelSerializer):
    quiblet = QuibletBasicSerializer(read_only=True)
    quibber = ProfileBasicSerializer(read_only=True)

    class Meta:
        model = Quib
        fields = '__all__'


class QuibHighlightedSerializer(serializers.ModelSerializer):
    class Meta:
        model = Quib
        fields = ('cover', 'title', 'id', 'slug', 'created_at')
