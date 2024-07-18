from django.contrib import admin
from django.urls import path, include
from drf_spectacular.views import SpectacularSwaggerView, SpectacularAPIView, SpectacularRedocView
from django.conf.urls.i18n import i18n_patterns
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('api/schema/', SpectacularAPIView.as_view(), name='schema'),
    path('docs/', SpectacularSwaggerView.as_view(url_name='schema'), name='docs'),
    path("redoc/", SpectacularRedocView.as_view(url_name='schema'), name='redoc'),
    path('i18n/', include('django.conf.urls.i18n')),
    path('account/', include('users.urls')),
    path('accounts/', include('allauth.urls')),
    path("admin/", admin.site.urls),
    path('pages/', include('django.contrib.flatpages.urls')),
    path('api/games/', include('apps.games.urls')),
]

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
