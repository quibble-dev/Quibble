from rest_framework import serializers


class CommentReactionResponseSerializer(serializers.Serializer):
    success = serializers.BooleanField()
