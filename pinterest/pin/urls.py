"""Pin URLs."""

# Django
from django.urls import include, path

# Django Rest framework
from rest_framework.routers import DefaultRouter

# Views
from pinterest.pin.api.views import pin as pin_view

# Set Routers
router = DefaultRouter()
router.register(r'pin', pin_view.PinViewSet, basename='pin')

urlpatterns = [
    path('', include(router.urls)),
]
