from rest_framework import serializers

from apps.user.api.v1.serializers import ProfileBasicSerializer

from ...models import Quiblet


class QuibletSerializer(serializers.ModelSerializer):
    class Meta:
        model = Quiblet
        fields = '__all__'


class QuibletBasicSerializer(serializers.ModelSerializer):
    class Meta:
        model = Quiblet
        fields = ('name', 'avatar')


class QuibletDetailedSerializer(serializers.ModelSerializer):
    rangers = ProfileBasicSerializer(many=True)
    quibs = serializers.SerializerMethodField()

    class Meta:
        model = Quiblet
        fields = '__all__'

    def get_quibs(self, obj) -> int:
        return obj.quibs.count()


class QuibletExistsSerializer(serializers.Serializer):
    exists = serializers.BooleanField()
    name = serializers.CharField()
