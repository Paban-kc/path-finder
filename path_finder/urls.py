from django.contrib import admin
from django.urls import path, include

# Specify the app_name for the included URLs
app_name = "auth_common"

urlpatterns = [
    path("admin/", admin.site.urls),
    path("users/", include("auth_common.urls")), 
    # path(
    #     "api/", include(("auth_common.urls"), namespace="api")
    # ), 
]
