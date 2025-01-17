from rest_framework import serializers

from apps.post.models import Post

from ...serializers.community import CommunityBasicSerializer
from ...serializers.user.profile import ProfileBasicSerializer


class PostSerializer(serializers.ModelSerializer):
    community = CommunityBasicSerializer(read_only=True)
    poster = ProfileBasicSerializer(read_only=True)

    class Meta:
        model = Post
        fields = '__all__'
