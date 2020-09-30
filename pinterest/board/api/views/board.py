"""Boards views."""

# Django REST Framework
from rest_framework import viewsets
# from rest_framework.generics import get_object_or_404

# Model
from pinterest.board.models import Board

# Serializers
from pinterest.board.api.serializers import (
    BoardModelSerializer,
    CreateUpdateBoardSerializer,
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


class BoardViewSet(
        CustomCreateModelMixin,
        CustomRetrieveModelMixin,
        CustomListModelMixin,
        CustomUpdateModelMixin,
        CustomDestroyModelMixin,
        viewsets.GenericViewSet):
    """Board view set.

       Crud for a boards
    """
    custom_actions = CustomActions()
    queryset = Board.objects.all()
    serializer_class = BoardModelSerializer

    def get_permissions(self):
        """Assign permission based on action."""
        permissions = [IsAuthenticated]
        return [permission() for permission in permissions]

    def get_serializer_class(self):
        """Return serializer based on action."""
        if self.action in ['create', 'update']:
            return CreateUpdateBoardSerializer
        return BoardModelSerializer

    def get_queryset(self):
        """Restrict list to public-only."""
        if self.action == 'list':
            return self.queryset.filter(status='active')
        return self.queryset
