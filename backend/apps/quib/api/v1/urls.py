from rest_framework.routers import DefaultRouter

from .viewsets import QuibViewSet

router = DefaultRouter()
router.register(r'', QuibViewSet)

urlpatterns = router.urls
