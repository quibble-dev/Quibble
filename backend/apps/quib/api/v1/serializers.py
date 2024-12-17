from rest_framework import serializers

from apps.quiblet.api.v1.serializers import QuibletSerializer, QuibletSlimSerializer

from ...models import Quib


class QuibSerializer(serializers.ModelSerializer):
    quiblet = QuibletSerializer(read_only=True)

    class Meta:
        model = Quib
        fields = '__all__'


class QuibSlimSerializer(serializers.ModelSerializer):
    quiblet = QuibletSlimSerializer(read_only=True)

    class Meta:
        model = Quib
        exclude = ('quibber',)
