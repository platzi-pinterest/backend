"""Board URLs."""

# Django
from django.urls import include, path

# Django Rest framework
from rest_framework.routers import DefaultRouter

# Views
from pinterest.board.api.views import board as board_view

# Set Routers
router = DefaultRouter()
router.register(r'board', board_view.BoardViewSet, basename='board')

urlpatterns = [
    path('', include(router.urls)),
]
