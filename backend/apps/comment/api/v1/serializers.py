from django.shortcuts import get_object_or_404
from rest_framework import serializers

from apps.user.api.v1.serializers import ProfileBasicSerializer

from ...models import Comment


class CommentSerializer(serializers.ModelSerializer):
    path = serializers.CharField(required=False)
    quibbler = ProfileBasicSerializer(read_only=True, allow_null=True)

    class Meta:
        model = Comment
        fields = '__all__'

    def create(self, validated_data):
        data = {
            'quibbler': validated_data.get('quibbler')
            or self.context['request'].user_profile,
            'content': validated_data['content'],
        }

        if path := validated_data.get('path'):
            parent_instance = get_object_or_404(Comment, path__match=path)
            comment_instance: Comment = Comment.objects.create_child(  # pyright: ignore
                parent=parent_instance, **data
            )
        else:
            comment_instance: Comment = Comment.objects.create_child(
                **data
            )  # pyright: ignore
        comment_instance.save()
        return comment_instance
