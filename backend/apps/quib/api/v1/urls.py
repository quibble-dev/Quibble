from rest_framework import routers

from .viewsets import QuibViewSet

router = routers.DefaultRouter()
router.register(r'', QuibViewSet)

urlpatterns = router.urls
