from rest_framework import serializers

from apps.quib.models import Quib


class QuibHighlightedSerializer(serializers.ModelSerializer):
    class Meta:
        model = Quib
        fields = ('cover', 'title', 'id', 'slug', 'created_at')
