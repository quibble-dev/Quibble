from rest_framework import serializers

from apps.quiblet.api.v1.mixins import QuibletSlimMixin
from apps.user.api.v1.serializers import ProfileMinimalSerializer

from ...models import Quib


class QuibSerializer(QuibletSlimMixin):
    class Meta:
        model = Quib
        fields = '__all__'


class QuibMinimalSerializer(QuibletSlimMixin):
    class Meta:
        model = Quib
        exclude = ('quibber',)


class QuibExtendedSerializer(QuibletSlimMixin):
    quibber = ProfileMinimalSerializer(read_only=True)

    class Meta:
        model = Quib
        fields = '__all__'


class QuibHighlightedSerializer(serializers.ModelSerializer):
    class Meta:
        model = Quib
        fields = ('cover', 'title', 'id', 'slug', 'created_at')
