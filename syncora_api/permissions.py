# Creates custom permission to check if the user is also the owner of an instance
# to allow editing, otherwise the view is read-only.
# Code adapted from the django rest framework documentation
# https://www.django-rest-framework.org/tutorial/4-authentication-and-permissions/
from rest_framework import permissions


class IsOwnerOrReadOnly(permissions.BasePermission):
    """
    Custom permission which only allows owners of an object to edit it.
    Otherwise, the object is read-only.
    """

    def has_object_permission(self, request, view, obj):
        # Read permissions are allowed to any request
        # and is considered one of the safe methods
        if request.method in permissions.SAFE_METHODS:
            return True

        # Write permissions are only allowed to the owner of the object
        return obj.user == request.user
