from rest_framework import serializers

from apps.quib.models import Quib

from ...serializers.community import QuibletBasicSerializer
from ...serializers.user.profile import ProfileBasicSerializer


class QuibSerializer(serializers.ModelSerializer):
    quiblet = QuibletBasicSerializer(read_only=True)
    quibber = ProfileBasicSerializer(read_only=True)

    class Meta:
        model = Quib
        fields = '__all__'
