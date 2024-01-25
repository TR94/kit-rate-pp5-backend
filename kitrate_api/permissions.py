from rest_framework import permissions 

# Taken from Code Institute lesson material on Django REST Framework

# Custom permission to define if a user is the owner of an object (data) or not
class IsOwnerOrReadOnly(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return True
        return obj.owner == request.user