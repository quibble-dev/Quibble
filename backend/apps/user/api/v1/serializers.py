from typing import Optional

from rest_framework import serializers

from ...models import Profile, User


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'email', 'password', 'date_joined')
        read_only_fields = ('date_joined',)
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        user = User.objects.create_user(**validated_data)  # pyright: ignore
        return user


class AuthSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('email', 'password')


class AuthTokenSerializer(serializers.Serializer):
    token = serializers.CharField()


class ProfileSerializer(serializers.ModelSerializer):
    user = UserSerializer(read_only=True)

    class Meta:
        model = Profile
        fields = '__all__'


class ProfileBasicSerializer(serializers.ModelSerializer):
    name = serializers.SerializerMethodField()

    class Meta:
        model = Profile
        fields = ('username', 'avatar', 'name')

    def get_name(self, obj) -> Optional[str]:
        if obj.first_name or obj.last_name:
            truthy_fields = filter(None, [obj.first_name, obj.last_name])
            return " ".join(truthy_fields)
        return None
