from rest_framework.routers import DefaultRouter
from collections_app.views import CollectionViewSet

router = DefaultRouter()
router.register(r'', CollectionViewSet, basename='collections')

urlpatterns = router.urls
