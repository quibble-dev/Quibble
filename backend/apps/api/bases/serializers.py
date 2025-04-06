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


class BaseRatioModelSerializer(serializers.ModelSerializer):
    """
    Base serializer for instances with ratio.
    Checks if it has annotated ratio or not, then proceeds to calculate it!
    """

    ratio = serializers.SerializerMethodField()

    def get_ratio(self, obj):
        if hasattr(obj, 'ratio'):
            return obj.ratio
        # for non-annotated instances (like new instances), calculate it!
        return obj.upvotes.count() - obj.downvotes.count()
