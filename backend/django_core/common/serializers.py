from rest_framework import serializers


class DetailResponseSerializer(serializers.Serializer):
    """Serializer for views returning just a response with detail key"""

    detail = serializers.CharField()
