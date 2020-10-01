"""Categories views."""

# Django REST Framework
from rest_framework import viewsets
# from rest_framework.generics import get_object_or_404

# Model
from pinterest.category.models import Category

# Serializers
from pinterest.category.api.serializers import (
    CategoryModelSerializer,
)

# Permissions
from rest_framework.permissions import IsAuthenticated

# Actions / Utils
from pinterest.utils import (
    CustomCreateModelMixin,
    CustomRetrieveModelMixin,
    CustomListModelMixin,
    CustomUpdateModelMixin,
    CustomDestroyModelMixin
)
from pinterest.utils.response import CustomActions


class CategoryViewSet(
        CustomCreateModelMixin,
        CustomRetrieveModelMixin,
        CustomListModelMixin,
        CustomUpdateModelMixin,
        CustomDestroyModelMixin,
        viewsets.GenericViewSet):
    """Category view set.

       Crud for a Categories
    """
    custom_actions = CustomActions()
    queryset = Category.objects.all()
    serializer_class = CategoryModelSerializer

    def get_permissions(self):
        """Assign permission based on action."""
        permissions = [IsAuthenticated]
        return [permission() for permission in permissions]

    def get_serializer_class(self):
        """Return serializer based on action."""
        return CategoryModelSerializer

    def get_queryset(self):
        """Restrict list to public-only."""
        if self.action == 'list':
            return self.queryset.filter(status='active')
        return self.queryset
