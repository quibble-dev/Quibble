from rest_framework.routers import DefaultRouter

from .viewsets import QuibModelViewSet

router = DefaultRouter()
router.register(r'', QuibModelViewSet)

urlpatterns = router.urls
