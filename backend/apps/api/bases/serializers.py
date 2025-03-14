from rest_framework import serializers


class DetailResponseSerializer(serializers.Serializer):
    """
    Serializer for a response containing a `"detail"` message.
    Used for generic informational responses.
    """

    detail = serializers.CharField()


class SuccessResponseSerializer(serializers.Serializer):
    """
    Serializer for a response with a `"success"` boolean.
    Typically used for confirming successful operations.
    """

    success = serializers.BooleanField()


class ReactionSerializer(serializers.Serializer):
    """
    Serializer for reactions.
    Used for posts/comments/etc...
    """

    action = serializers.CharField()

    def validate_action(self, value):
        if value not in ['upvote', 'downvote']:
            raise serializers.ValidationError(f'Invalid action: {value}')
        return value
