from rest_framework import serializers

from apps.quib.models import Quib
from apps.quiblet.api.v1.serializers import QuibletBasicSerializer
from apps.user.api.v1.serializers import ProfileBasicSerializer


class QuibSerializer(serializers.ModelSerializer):
    quiblet = QuibletBasicSerializer(read_only=True)
    quibber = ProfileBasicSerializer(read_only=True)

    class Meta:
        model = Quib
        fields = '__all__'
