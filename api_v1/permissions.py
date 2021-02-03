from rest_framework import permissions


class TokenIsOwnerAndReadOnly(permissions.BasePermission):
    def has_permission(self, request, view):
        if request.method not in permissions.SAFE_METHODS:
            return False
        if request.auth:
            return True
