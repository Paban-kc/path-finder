from .Views import (
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
    re_path(
        r"^password-reset/(?P<uidb36>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,32})/$",  # noqa: E501
        TemplateView.as_view(),
        name="confirm_password_template",
    ),
    path("auth/login/", LoginView.as_view(), name="login"),
    path("auth/logout/", LogoutView.as_view(), name="logout"),
    path("auth/register/", RegisterView.as_view(), name="register"),
    path("auth/reset_password/", ResetPasswordView.as_view(), name="reset_password"),
    path("auth/user_profile/", UserProfileView.as_view(), name="user_profile"),
    path(
        "auth/change_password/",
        UserChangePasswordView.as_view(),
        name="change_password",
    ),
]
