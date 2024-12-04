from rest_framework.routers import DefaultRouter

from .viewsets import QuibletViewSet

app_name = 'quiblet_api_v1'

router = DefaultRouter()
router.register('', QuibletViewSet, basename='quiblet')

urlpatterns = []
urlpatterns += router.urls
