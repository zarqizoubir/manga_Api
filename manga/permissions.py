from rest_framework import permissions
from rest_framework.request import HttpRequest
from django.contrib.auth.models import User


class IsAdminOrReadOnly(permissions.BasePermission):

    def has_permission(self, request: HttpRequest, view):

        if request.user.is_authenticated:

            if request.user.is_superuser:
                return True

            if request.method in permissions.SAFE_METHODS:
                return True

        return False
