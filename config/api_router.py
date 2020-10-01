from django.conf import settings
from rest_framework.routers import DefaultRouter, SimpleRouter

from pinterest.users.api.views import UserViewSet
from pinterest.board.api.views import BoardViewSet
from pinterest.category.api.views import CategoryViewSet
from pinterest.pin.api.views import PinViewSet

if settings.DEBUG:
    router = DefaultRouter()
else:
    router = SimpleRouter()

router.register("users", UserViewSet)
router.register("board", BoardViewSet)
router.register("category", CategoryViewSet)
router.register("pin", PinViewSet)

app_name = "api"
urlpatterns = router.urls
