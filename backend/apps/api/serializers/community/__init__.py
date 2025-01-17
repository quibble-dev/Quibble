from rest_framework import serializers

from apps.community.models import Community

from ...serializers.user.profile import ProfileBasicSerializer


class CommunitySerializer(serializers.ModelSerializer):
    class Meta:
        model = Community
        fields = '__all__'


class CommunityBasicSerializer(serializers.ModelSerializer):
    class Meta:
        model = Community
        fields = ('name', 'avatar')


class CommunityDetailedSerializer(serializers.ModelSerializer):
    rangers = ProfileBasicSerializer(many=True)
    quibs = serializers.SerializerMethodField()

    class Meta:
        model = Community
        fields = '__all__'

    def get_quibs(self, obj) -> int:
        return obj.quibs.count()


class CommunityExistsSerializer(serializers.Serializer):
    exists = serializers.BooleanField()
    name = serializers.CharField()
