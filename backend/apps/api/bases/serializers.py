from rest_framework import serializers


class DetailResponseSerializer(serializers.Serializer):
    detail = serializers.CharField()


class SuccessResponseSerializer(serializers.Serializer):
    success = serializers.BooleanField()
