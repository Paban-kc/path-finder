from auth_common.Views.application.applicationView import ApplicationApplyViewSet
from auth_common.Views.feedback.feedbackView import FeedbackViewSet
from auth_common.Views.internship_submission.internshipSubmissionView import (
    InternshipSubmissionViewSet,
)
from auth_common.Views.placement.placementView import PlacementFromApplicationView
from auth_common.Views.user_profile.userProfileView import RegisterEditProfileViewSet
from .Views.auth import (
    LoginView,
    LogoutView,
    RegisterView,
    UserProfileView,
    UserChangePasswordView,
    ResetPasswordView,
)
from django.urls import path, re_path


urlpatterns = [
    path("auth/login/", LoginView.as_view(), name="login"),
    path("auth/logout/", LogoutView.as_view(), name="logout"),
    path("auth/register/", RegisterView.as_view(), name="register"),
    path("auth/reset-password/", ResetPasswordView.as_view(), name="reset-password"),
    path("auth/user-profile/", UserProfileView.as_view(), name="user-profile"),
    path(
        "auth/change_password/",
        UserChangePasswordView.as_view(),
        name="change_password",
    ),
    # others
    path(
        "auth/register-profile/",
        RegisterEditProfileViewSet.as_view(
            {
                "get": "list",
                "post": "create",
                "put": "update_profile",
                "patch": "partial_update",
            }
        ),
        name="register-profile",
    ),
    path(
        "auth/internship-submission/",
        InternshipSubmissionViewSet.as_view(
            {
                "get": "list",
                "post": "create",
            }
        ),
        name="internship-submission",
    ),
    path(
        "auth/application-apply/",
        ApplicationApplyViewSet.as_view(
            {
                "get": "list",
                "post": "create",
                "patch": "partial_update",
                "delete": "destroy",
            }
        ),
        name="application-apply",
    ),
    path(
        "auth/placement/",
        PlacementFromApplicationView.as_view(
            {
                "get": "list",
                "post": "create",
                "patch": "partial_update",
                "delete": "destroy",
            }
        ),
        name="placement",
    ),
    path(
        "auth/feedback/",
        FeedbackViewSet.as_view(
            {
                "get": "list",
                "post": "create",
                "patch": "partial_update",
                "delete": "destroy",
            }
        ),
        name="feedback",
    ),
]
