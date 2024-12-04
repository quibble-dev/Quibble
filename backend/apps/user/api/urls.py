from django.urls import path
from rest_framework.routers import DefaultRouter

from .views import LoginAPIView, LogoutAPIView, MeAPIView, RegisterAPIView
from .viewsets import MyProfilesViewSet, ProfileViewSet, UserViewSet

# main router for users/ and profiles/
router = DefaultRouter()

router.register(r'', UserViewSet)
router.register(r'profiles', ProfileViewSet)
# profiles of requested user
router.register(r'me/profiles', MyProfilesViewSet, basename='me-profile')

# fmt: off
urlpatterns = [
    # auth endpoints
    path('login/', LoginAPIView.as_view(), name='login'),
    path('logout/', LogoutAPIView.as_view(), name='logout'),
    path('register/', RegisterAPIView.as_view(), name='register'),
    # user view of requested user
    path('me/', MeAPIView.as_view(), name='me'),
]
# fmt: on

# router urls should be placed last to prevent overriding
urlpatterns += router.urls
