from django.shortcuts import get_object_or_404
from rest_framework import serializers

from apps.comment.models import Comment

from ...serializers.user.profile import ProfileBasicSerializer


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


class CommentDetailSerializer(serializers.ModelSerializer):
    commenter = ProfileBasicSerializer(allow_null=True)
    ratio = serializers.IntegerField()

    class Meta:
        model = Comment
        fields = '__all__'
