from rest_framework import serializers

from apps.quib.models import Quib


class QuibSerializer(serializers.ModelSerializer):
    class Meta:
        model = Quib
        fields = '__all__'
