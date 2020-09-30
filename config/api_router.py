from django.conf import settings
from rest_framework.routers import DefaultRouter, SimpleRouter

from pinterest.users.api.views import UserViewSet
from pinterest.board.api.views import BoardViewSet

if settings.DEBUG:
    router = DefaultRouter()
else:
    router = SimpleRouter()

router.register("users", UserViewSet)
router.register("board", BoardViewSet)


app_name = "api"
urlpatterns = router.urls
