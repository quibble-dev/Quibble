from rest_framework.permissions import SAFE_METHODS, BasePermission


class IsRangerOrReadOnly(BasePermission):
    """
    Custom permission to allow only rangers of a Quiblet to edit it.
    """

    def has_permission(self, request, view):  # type: ignore
        if request.method in SAFE_METHODS:
            return True

        return bool(request.user and request.user.is_authenticated)

    def has_object_permission(self, request, view, obj):  # type: ignore
        if request.method in SAFE_METHODS:
            return True

        user_profile = getattr(request, 'user_profile', None)
        if user_profile is None:
            return False

        return obj.rangers.filter(id=request.user_profile.id).exists()
