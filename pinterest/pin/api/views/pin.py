"""Pins views."""

# Django REST Framework
from rest_framework import viewsets
# from rest_framework.generics import get_object_or_404

# Model
from pinterest.pin.models import Pin

# Serializers
from pinterest.pin.api.serializers import (
    PinModelSerializer,
    CreateUpdatePinSerializer,
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


class PinViewSet(
        CustomCreateModelMixin,
        CustomRetrieveModelMixin,
        CustomListModelMixin,
        CustomUpdateModelMixin,
        CustomDestroyModelMixin,
        viewsets.GenericViewSet):
    """Pin view set.

       Crud for a pins
    """
    custom_actions = CustomActions()
    queryset = Pin.objects.all()
    serializer_class = PinModelSerializer

    def get_permissions(self):
        """Assign permission based on action."""
        permissions = [IsAuthenticated]
        return [permission() for permission in permissions]

    def get_serializer_class(self):
        """Return serializer based on action."""
        if self.action in ['create', 'update']:
            return CreateUpdatePinSerializer
        return PinModelSerializer

    def get_queryset(self):
        """Restrict list to public-only."""
        if self.action == 'list':
            return self.queryset.filter(status='active')
        return self.queryset
