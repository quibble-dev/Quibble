from rest_framework.permissions import SAFE_METHODS, BasePermission


class IsQuibblerOrReadOnly(BasePermission):
    """
    Custom permission to allow only quibbler of a feature to edit it.
    """

    def has_object_permission(self, request, view, obj):
        if request.method in SAFE_METHODS:
            return True

        return obj.quibbler == request.user_profile
