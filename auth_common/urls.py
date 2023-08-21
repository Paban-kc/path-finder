from auth_common.Views.organization_profile.organizationProfileViewSet import OrganizationProfileViewSet
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
from .Views.student_profile import StudentProfileViewSet


urlpatterns = [
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
    # others
    path(
        "auth/student-profile/",
        StudentProfileViewSet.as_view({"get": "list", "post": "create"}),
        name="student-profile",
    ),
    path(
        "auth/organization-profile/",
        OrganizationProfileViewSet.as_view({"get": "list", "post": "create"}),
        name="organization-profile",
    ),
]
