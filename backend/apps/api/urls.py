from django.urls import include, path
from rest_framework import routers

from .views.user import MeAPIView
from .views.user.auth import LoginAPIView, LogoutAPIView, RegisterAPIView
from .viewsets.comment import CommentViewSet
from .viewsets.community import CommunityViewSet
from .viewsets.post import PostViewSet
from .viewsets.user import MyProfilesViewSet, ProfileViewSet

main_router = routers.DefaultRouter()
main_router.register(r'comments', CommentViewSet, basename='comments')
main_router.register(r'posts', PostViewSet, basename='posts')
main_router.register(r'communities', CommunityViewSet, basename='communities')
# user routes
user_router = routers.DefaultRouter()
user_router.register(r'u/profiles', ProfileViewSet, basename='profiles')
user_router.register(r'u/me/profiles', MyProfilesViewSet, basename='me-profiles')

# https://stackoverflow.com/a/65186703
main_router.registry.extend(user_router.registry)

# fmt: off
urlpatterns = [
    path('u/', include([
        # auth
        path('login/', LoginAPIView.as_view(), name='login'),
        path('logout/', LogoutAPIView.as_view(), name='logout'),
        path('register/', RegisterAPIView.as_view(), name='register'),
        # user view of requested user
        path('me/', MeAPIView.as_view(), name='me'),
    ])),
]
# fmt: on

# router urls should be placed last to prevent overriding
urlpatterns += main_router.urls
