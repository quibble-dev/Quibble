from rest_framework import serializers


class QuibletExistsSerializer(serializers.Serializer):
    exists = serializers.BooleanField()
    name = serializers.CharField()
