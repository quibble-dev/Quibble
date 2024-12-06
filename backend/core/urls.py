from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import include, path
from drf_spectacular.views import SpectacularAPIView, SpectacularSwaggerView

# modify adminsite
admin.site.site_header = 'Quibble Administration'
admin.site.index_title = 'Apps and Services'
admin.site.site_title = 'Quibble'

urlpatterns = [
    # admin
    path('admin/', admin.site.urls),
    # api endpoints
    path(
        'api/',
        include(
            [
                path('users/', include('apps.user.api.urls')),
                path('quiblets/', include('apps.quiblet.api.urls')),
            ]
        ),
    ),
    # openapi
    path('api/schema/', SpectacularAPIView.as_view(), name='schema'),
    path('api/schema/swagger', SpectacularSwaggerView.as_view(), name='swagger'),
]
# https://docs.djangoproject.com/en/2.1/howto/static-files/#serving-static-files-during-development
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
