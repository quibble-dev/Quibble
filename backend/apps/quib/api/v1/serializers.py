from rest_framework import serializers

from apps.quiblet.api.v1.serializers import (
    QuibletModelSerializer,
    QuibletSlimModelSerializer,
)

from ...models import QuibModel


class QuibModelSerializer(serializers.ModelSerializer):
    quiblet = QuibletModelSerializer(read_only=True)

    class Meta:
        model = QuibModel
        fields = '__all__'


class QuibSlimModelSerializer(serializers.ModelSerializer):
    quiblet = QuibletSlimModelSerializer(read_only=True)

    class Meta:
        model = QuibModel
        exclude = ('quibber',)
