"""Category URLs."""

# Django
from django.urls import include, path

# Django Rest framework
from rest_framework.routers import DefaultRouter

# Views
from pinterest.category.api.views import category as category_view

# Set Routers
router = DefaultRouter()
router.register(r'category', category_view.CategoryViewSet, basename='category')

urlpatterns = [
    path('', include(router.urls)),
]
