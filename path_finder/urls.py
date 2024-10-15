from django.contrib import admin
from django.urls import path, include
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from django.conf import settings
from django.conf.urls.static import static

info = openapi.Info(
    title="Path-Finder API",
    default_version="v1",
    description="API Documentation for Path-Finder",
    terms_of_service="Your terms of service URL",
    contact=openapi.Contact(email="your-email@example.com"),
    license=openapi.License(name="Your License"),
)

schema_view = get_schema_view(
    info=info,
    public=True,
    permission_classes=(permissions.AllowAny,),
)

urlpatterns = [
    path("admin/", admin.site.urls),
    path("docs", schema_view.with_ui("swagger", cache_timeout=0),
         name="schema-swagger-ui"),
    # path("users/", include("auth_common.urls")),
    # path("admin", admin.site.urls),
    path(
        "api-documentation",
        schema_view.with_ui("swagger", cache_timeout=0),
        name="schema-swagger-ui",
    ),
    path("", include("auth_common.urls")),
    # path("api/", include(("auth_common.urls"), namespace="api")),
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
