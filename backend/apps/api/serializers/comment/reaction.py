from rest_framework import serializers


class CommentReactionSerializer(serializers.Serializer):
    action = serializers.CharField()
