from django.urls import include, path
from rest_framework.routers import DefaultRouter

from . import views

router = DefaultRouter()
router.register(r'users', views.UserViewSet, basename='user')
router.register(r'profiles', views.ProfileViewSet, basename='profile')

urlpatterns = [
    path('', include(router.urls)),
]
