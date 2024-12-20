from rest_framework import serializers

from .serializers import QuibletMinimalSerializer


class QuibletSlimMixin(serializers.ModelSerializer):
    quiblet = QuibletMinimalSerializer(read_only=True)
