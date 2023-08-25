from auth_common.Views.edit_profile.RegisterEditProfileView import RegisterEditProfileViewSet
from .Views.auth import (
    LoginView,
    LogoutView,
    RegisterView,
    UserProfileView,
    UserChangePasswordView,
    ResetPasswordView,
)
from django.urls import path, re_path
from django.views.generic import TemplateView


urlpatterns = [
    path("auth/login/", LoginView.as_view(), name="login"),
    path("auth/logout/", LogoutView.as_view(), name="logout"),
    path("auth/register/", RegisterView.as_view(), name="register"),
    path("auth/reset-password/", ResetPasswordView.as_view(), name="reset-password"),
    path("auth/user-profile/", UserProfileView.as_view(), name="user-profile"),
    path(
        "auth/register-profile/",
        RegisterEditProfileViewSet.as_view({"get": "list", "post": "create"}),
        name="register-profile",
    ),
    path(
        "auth/change_password/",
        UserChangePasswordView.as_view(),
        name="change_password",
    ),

]
