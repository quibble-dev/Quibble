from rest_framework import serializers

from apps.user.models import User


class AuthSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('email', 'password')


class AuthTokenSerializer(serializers.Serializer):
    token = serializers.CharField()
