from rest_framework.routers import DefaultRouter
from .views import UnifiedProductViewSet

router = DefaultRouter()
router.register(r'products', UnifiedProductViewSet)

urlpatterns = router.urls
