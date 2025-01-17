from rest_framework import routers

from .viewsets.comment import CommentViewSet
from .viewsets.post import QuibViewSet

router = routers.DefaultRouter()
router.register(r'comments', CommentViewSet)
router.register(r'post', QuibViewSet)

urlpatterns = router.urls
