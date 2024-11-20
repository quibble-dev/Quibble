from django.urls import include, path
from rest_framework.routers import DefaultRouter

from . import viewsets, views

# main router for users/ and profiles/
router = DefaultRouter()

router.register('users', viewsets.UserViewSet, basename='user')
router.register('profiles', viewsets.ProfileViewSet, basename='profile')
# profiles of requested user
router.register('me/profiles', viewsets.MyProfilesViewSet, basename='my-profiles')

# fmt: off
urlpatterns = [
    # knox routes with custom view
    path('auth/', include([
        path('login/', views.LoginAPIView.as_view(), name='login'),
        path('logout/', views.LogoutAPIView.as_view(), name='logout'),
    ])),
    # user view of requested user
    path('me/', views.MeAPIView.as_view(), name='me'),
]
# fmt: on

# router urls should be placed last to prevent overriding
urlpatterns += router.urls
