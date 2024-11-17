from django.urls import include, path
from rest_framework.routers import DefaultRouter

from . import views

# main router for users/ and profiles/
router = DefaultRouter()

router.register('users', views.UserViewSet, basename='user')
router.register('profiles', views.ProfileViewSet, basename='profile')
# profiles of requested user
router.register('me/profiles', views.MyProfilesViewSet, basename='my-profiles')

# fmt: off
urlpatterns = [
    # knox routes with custom view
    path('auth/', include([
        path('login/', views.LoginView.as_view(), name='login'),
        path('logout/', views.LogoutView.as_view(), name='logout'),
    ])),
    # user view of requested user
    path('me/', views.MeView.as_view(), name='me'),
]
# fmt: on

# router urls should be placed last to prevent overriding
urlpatterns += router.urls
