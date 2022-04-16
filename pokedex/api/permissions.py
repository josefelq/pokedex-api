from rest_framework import permissions


class IsOwnerOrReadOnly(permissions.BasePermission):
    """
    Object-level permission to only allow owners of an object to edit it.
    Assumes the model instance has a `discovered_by` attribute.
    """

    def has_permission(self, request, view) -> bool:
        """Permissions for list methods."""
        if request.method in permissions.SAFE_METHODS:
            return True
        return request.user.is_authenticated

    def has_object_permission(self, request, view, obj):
        """Permissions used for single object."""
        if request.method in permissions.SAFE_METHODS:
            return True
        # Instance must have an attribute named `discovered_by`.
        return obj.discovered_by == request.user
