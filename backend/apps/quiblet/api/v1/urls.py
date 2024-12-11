from rest_framework.routers import DefaultRouter

from .viewsets import QuibletViewSet, QuibViewSet

router = DefaultRouter()
router.register(r'quiblets', QuibletViewSet)
router.register(r'quibs', QuibViewSet)

urlpatterns = router.urls
