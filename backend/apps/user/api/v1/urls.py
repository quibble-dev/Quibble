from django.urls import include, path
from rest_framework.routers import DefaultRouter

from .views import LoginAPIView, LogoutAPIView, MeAPIView, RegisterAPIView
from .viewsets import MyProfilesModelViewSet, ProfileModelReadOnlyViewSet

router = DefaultRouter()
router.register(r'profiles', ProfileModelReadOnlyViewSet)
router.register(r'me/profiles', MyProfilesModelViewSet, basename='me-profile')

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
