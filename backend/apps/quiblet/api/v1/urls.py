from rest_framework.routers import DefaultRouter

from .viewsets import QuibletViewSet

router = DefaultRouter()
router.register(r'quiblets', QuibletViewSet)

urlpatterns = router.urls
