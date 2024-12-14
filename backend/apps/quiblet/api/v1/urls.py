from rest_framework.routers import DefaultRouter

from .viewsets import QuibletModelViewSet

router = DefaultRouter()
router.register(r'', QuibletModelViewSet)

urlpatterns = router.urls
