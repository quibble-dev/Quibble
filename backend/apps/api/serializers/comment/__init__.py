from django.shortcuts import get_object_or_404
from rest_framework import serializers

from apps.comment.models import Comment
from apps.post.models import Post

from ...serializers.user.profile import ProfileBasicSerializer


class CommentSerializer(serializers.ModelSerializer):
    commenter = ProfileBasicSerializer(allow_null=True)
    ratio = serializers.IntegerField()

    class Meta:
        model = Comment
        fields = '__all__'


class CommentOverviewSerializer(CommentSerializer):
    commenter = serializers.SerializerMethodField()
    post = serializers.SerializerMethodField()
    reply_to = serializers.SerializerMethodField()

    class Meta(CommentSerializer.Meta):
        fields = (
            'id',
            'commenter',
            'reply_to',
            'ratio',
            'post',
            'created_at',
            'content',
            'deleted',
        )

    def get_commenter(self, obj):
        return obj.commenter.username

    def get_post(self, obj):
        request = self.context.get('request')

        if post := Post.objects.filter(comments=obj).first():
            return {
                "title": post.title,
                "slug": post.slug,
                "community": {
                    "name": post.community.name,
                    "avatar": (
                        request.build_absolute_uri(post.community.avatar.url)
                        if post.community.avatar
                        else None
                    ),
                },
            }
        return None

    def get_reply_to(self, obj):
        if parent := obj.parent():
            return parent.commenter.username
        return None


class CommentCreateSerializer(serializers.ModelSerializer):
    path = serializers.CharField(required=False)

    class Meta:
        model = Comment
        fields = ('path', 'content')

    def create(self, validated_data):
        data = {
            'commenter': self.context['request'].user_profile,
            'content': validated_data['content'],
        }

        if path := validated_data.get('path'):
            parent_instance = get_object_or_404(Comment, path__match=path)
            comment_instance: Comment = Comment.objects.create_child(  # pyright: ignore
                parent=parent_instance, **data
            )
        else:
            comment_instance: Comment = Comment.objects.create_child(**data)  # pyright: ignore

        comment_instance.upvotes.add(data['commenter'])
        return comment_instance
