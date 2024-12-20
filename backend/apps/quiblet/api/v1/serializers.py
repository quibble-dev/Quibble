from typing import Optional

from rest_framework import serializers

from apps.user.models import Profile

from ...models import Quiblet


class RangerSerializer(serializers.ModelSerializer):
    name = serializers.SerializerMethodField()

    class Meta:
        model = Profile
        fields = ('username', 'avatar', 'name')

    def get_name(self, obj) -> Optional[str]:
        if obj.first_name or obj.last_name:
            truthy_fields = filter(None, [obj.first_name, obj.last_name])
            return " ".join(truthy_fields)
        return None


class QuibletSerializer(serializers.ModelSerializer):
    class Meta:
        model = Quiblet
        fields = '__all__'


class QuibletMinimalSerializer(serializers.ModelSerializer):
    class Meta:
        model = Quiblet
        fields = ('name', 'avatar')


class QuibletExtendedSerializer(serializers.ModelSerializer):
    rangers = RangerSerializer(many=True)
    quibs = serializers.SerializerMethodField()

    class Meta:
        model = Quiblet
        fields = '__all__'

    def get_quibs(self, obj) -> int:
        return obj.quibs.count()


class QuibletExistsSerializer(serializers.Serializer):
    exists = serializers.BooleanField()
    name = serializers.CharField()
