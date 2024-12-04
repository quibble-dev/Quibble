from rest_framework.routers import DefaultRouter

from .viewsets import QuibletViewSet

router = DefaultRouter()
router.register(r'', QuibletViewSet)

urlpatterns = []
urlpatterns += router.urls
