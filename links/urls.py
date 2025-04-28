
from rest_framework.routers import DefaultRouter
from links.views import LinkViewSet

router = DefaultRouter()
router.register(r'', LinkViewSet, basename='links')

urlpatterns = router.urls
