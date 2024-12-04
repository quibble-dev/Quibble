from rest_framework.serializers import ModelSerializer

from apps.quiblet.models import Quiblet


class QuibletSerializer(ModelSerializer):
    class Meta:
        model = Quiblet
        fields = '__all__'
