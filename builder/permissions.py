from rest_framework.permissions import BasePermission

class IsOwnerOfPortfolio(BasePermission):
    """
    Checks if the authenticated user owns the portfolio of the object.
    """

    def has_object_permission(self, request, view, obj):
        return obj.portfolio.user == request.user
