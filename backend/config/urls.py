from django.contrib import admin
from django.urls import include, path
from drf_spectacular.views import SpectacularAPIView, SpectacularSwaggerView

# fmt: off
urlpatterns = [
    # admin
    path('admin/', admin.site.urls),
    # api endpoints
    path('api/', include([
        # v1 endpoints
        path('v1/', include(([
            path('user/', include('apps.user.api.v1.urls', namespace='user')),
        ], 'v1'), namespace='v1')),
    ])),
    # openapi
    path('api/schema/', SpectacularAPIView.as_view(api_version='v1'), name='schema'),
    path('api/schema/swagger', SpectacularSwaggerView.as_view(), name='swagger'),
]
# fmt: on
