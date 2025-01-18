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
    posts_count = serializers.SerializerMethodField()

    class Meta:
        model = Community
        fields = '__all__'

    def get_posts_count(self, obj) -> int:
        return obj.posts.count()


class CommunityExistsSerializer(serializers.Serializer):
    exists = serializers.BooleanField()
    name = serializers.CharField()
