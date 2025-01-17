from rest_framework import routers

from .viewsets.comment import CommentViewSet
from .viewsets.post import QuibViewSet
from .viewsets.quiblet import QuibletViewSet

router = routers.DefaultRouter()
router.register(r'comments', CommentViewSet)
router.register(r'post', QuibViewSet)
router.register(r'community', QuibletViewSet)

urlpatterns = router.urls
