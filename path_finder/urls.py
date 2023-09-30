from django.contrib import admin
from django.urls import path, include
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

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
    path("api-documentation/", schema_view.with_ui("swagger", cache_timeout=0),
         name="schema-swagger-ui"),
    path("users/", include("auth_common.urls")),
    # path("api/", include(("auth_common.urls"), namespace="api")),
]
