from rest_framework import serializers

from apps.user.models import Profile

from ...models import Quiblet


class RangerSerializer(serializers.ModelSerializer):
    name = serializers.SerializerMethodField()

    class Meta:
        model = Profile
        fields = ('username', 'avatar', 'name')

    def get_name(self, obj):
        if obj.first_name or obj.last_name:
            truthy_fields = filter(None, [obj.first_name, obj.last_name])
            return " ".join(truthy_fields)
        return None


class QuibletDetailSerializer(serializers.ModelSerializer):
    rangers = RangerSerializer(many=True)

    class Meta:
        model = Quiblet
        fields = '__all__'


class QuibletSerializer(serializers.ModelSerializer):
    class Meta:
        model = Quiblet
        fields = '__all__'


class QuibletSlimSerializer(serializers.ModelSerializer):
    class Meta:
        model = Quiblet
        fields = ('name', 'avatar')


class QuibletExistsSerializer(serializers.Serializer):
    exists = serializers.BooleanField()
    name = serializers.CharField()
