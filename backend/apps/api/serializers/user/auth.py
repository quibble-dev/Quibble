from dj_rest_auth.registration.serializers import (
    RegisterSerializer as RestAuthRegisterSerializer,
)
from dj_rest_auth.serializers import LoginSerializer as RestAuthLoginSerializer
from rest_framework import serializers

from apps.user.models import User


class AuthSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('email', 'password')

    def create(self, validated_data):
        user = User.objects.create_user(**validated_data)  # pyright: ignore
        return user


class AuthTokenSerializer(serializers.Serializer):
    token = serializers.CharField()


class LoginSerializer(RestAuthLoginSerializer):
    """Custom LoginSerializer making email field required and removing username field"""

    username = None
    email = serializers.EmailField(required=True)


class RegisterSerializer(RestAuthRegisterSerializer):
    """Custom RegisterSerializer removing username field"""

    username = None
