from django.urls import include, path
from rest_framework.routers import DefaultRouter

from knox import views as knox_views
from . import views

router = DefaultRouter()
router.register(r'users', views.UserViewSet, basename='user')
router.register(r'profiles', views.ProfileViewSet, basename='profile')

# fmt: off
urlpatterns = [
    path(r'auth/', include([
        # knox routes with custom view
        path('login/', views.CustomKnoxLoginView.as_view(), name='knox_login'),
        path('logout/', knox_views.LogoutView.as_view(), name='knox_logout'),
        path(
            'logout-all/',
            knox_views.LogoutAllView.as_view(),
            name='knox_logout_all',
        ),
    ])),
]
# fmt: on

# router urls should be placed last to prevent overriding
urlpatterns += router.urls
