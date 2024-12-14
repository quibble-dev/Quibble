from rest_framework import routers

from .viewsets import CommentModelViewSet

router = routers.DefaultRouter()
router.register(r'', CommentModelViewSet)

urlpatterns = router.urls
