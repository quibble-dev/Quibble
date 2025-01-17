from rest_framework import routers

from .viewsets.comment import CommentViewSet

router = routers.DefaultRouter()
router.register(r'comments', CommentViewSet)

urlpatterns = router.urls
