from rest_framework.routers import DefaultRouter

from .viewsets import QuibViewSet

router = DefaultRouter()
router.register(r'quibs', QuibViewSet)

urlpatterns = router.urls
