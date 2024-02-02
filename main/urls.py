from django.contrib import admin
from django.shortcuts import redirect
from django.urls import path, include
from drf_spectacular.views import SpectacularAPIView, SpectacularSwaggerView

urlpatterns = [
    path('admin/', admin.site.urls),
    path("docs/schema/", SpectacularAPIView.as_view(), name="schema"),
    path("docs/", SpectacularSwaggerView.as_view(url_name="schema"), name="swagger-ui"),

    path("clients/", include("client.urls")),
    path("mailings/", include("mailing.urls")),
    path("auth/", include("core.urls")),
    path('', include('django_prometheus.urls')),
    path('', lambda req: redirect('docs/')),
]
