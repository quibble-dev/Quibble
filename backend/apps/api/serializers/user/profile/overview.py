import copy

from rest_framework import serializers

from apps.api.serializers.comment import CommentDetailSerializer
from apps.api.serializers.post import PostSerializer


class OverviewSerializer(serializers.Serializer):
    type = serializers.CharField()
    data = serializers.SerializerMethodField()

    def get_data(self, obj):
        obj_type = obj.type
        obj_copy = copy.copy(obj)

        delattr(obj_copy, "type")

        if obj_type == "post":
            return PostSerializer(obj_copy, context=self.context).data
        return CommentDetailSerializer(obj_copy, context=self.context).data
