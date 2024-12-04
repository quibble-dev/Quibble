from django.urls import include, path
from rest_framework.routers import DefaultRouter

from .views import LoginAPIView, LogoutAPIView, MeAPIView, RegisterAPIView
from .viewsets import MyProfilesViewSet, ProfileViewSet, UserViewSet

router = DefaultRouter()
router.register(r'users', UserViewSet)
router.register(r'profiles', ProfileViewSet)
router.register(r'me/profiles', MyProfilesViewSet, basename='me-profile')

urlpatterns = [
    # auth endpoints
    path(
        'auth/',
        include(
            [
                path('login/', LoginAPIView.as_view(), name='login'),
                path('logout/', LogoutAPIView.as_view(), name='logout'),
                path('register/', RegisterAPIView.as_view(), name='register'),
            ]
        ),
    ),
    # user view of requested user
    path('me/', MeAPIView.as_view(), name='me'),
]

# router urls should be placed last to prevent overriding
urlpatterns += router.urls
