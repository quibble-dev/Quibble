from django.urls import path
from rest_framework.routers import DefaultRouter

from . import views, viewsets

# main router for users/ and profiles/
router = DefaultRouter()

router.register(r'', viewsets.UserViewSet)
router.register(r'profiles', viewsets.ProfileViewSet)
# profiles of requested user
router.register(r'me/profiles', viewsets.MyProfilesViewSet, basename='me-profile')

# fmt: off
urlpatterns = [
    # auth endpoints
    path('login/', views.LoginAPIView.as_view(), name='login'),
    path('logout/', views.LogoutAPIView.as_view(), name='logout'),
    path('register/', views.RegisterAPIView.as_view(), name='register'),
    # user view of requested user
    path('me/', views.MeAPIView.as_view(), name='me'),
]
# fmt: on

# router urls should be placed last to prevent overriding
urlpatterns += router.urls
