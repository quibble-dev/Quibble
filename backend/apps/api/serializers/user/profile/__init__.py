from typing import Optional

from rest_framework import serializers

from apps.api.serializers.user import UserSerializer
from apps.user.models import Profile


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
