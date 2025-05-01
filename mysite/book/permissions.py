
from rest_framework import permissions


class CheckAgencyCreate(permissions.BasePermission):
    def has_permission(self, request, view):
        if request.user.user_role == 'owner':
            return True
        return False

