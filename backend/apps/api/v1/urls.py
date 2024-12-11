from django.urls import include, path
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
    TokenVerifyView,
)

urlpatterns = [
    path('users/', include('apps.user.api.v1.urls')),
    path('quiblets/', include('apps.quiblet.api.v1.urls')),
    path('quibs/', include('apps.quib.api.v1.urls')),
    # jwt auth
    path(
        'auth/',
        include(
            [
                path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
                path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
                path('token/verify/', TokenVerifyView.as_view(), name='token_verify'),
            ]
        ),
    ),
]
