from rest_framework import serializers


class CommentReactionSerializer(serializers.Serializer):
    action = serializers.CharField()

    def validate_action(self, value):
        if not value in ['upvote', 'downvote']:
            raise serializers.ValidationError(f'Invalid action: {value}')
        return value
