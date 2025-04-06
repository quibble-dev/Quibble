from rest_framework import serializers

from apps.api.bases.serializers import BaseRatioModelSerializer
from apps.api.serializers.community import CommunityBasicSerializer
from apps.api.serializers.user.profile import ProfileBasicSerializer
from apps.post.models import Post


class PostSerializer(BaseRatioModelSerializer):
    community = CommunityBasicSerializer(read_only=True)
    poster = ProfileBasicSerializer(read_only=True)

    class Meta:
        model = Post
        fields = '__all__'

    def get_ratio(self, obj):
        if hasattr(obj, 'ratio'):
            return obj.ratio
        # for non-annotated instances (like new posts), calculate it!
        return obj.upvotes.count() - obj.downvotes.count()


class PostCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = ('community', 'poster', 'title', 'content', 'cover')

    def create(self, validated_data):
        poster = self.context['request'].user_profile
        post = Post.objects.create(**validated_data)

        post.upvotes.add(poster)

        return post
