from django.urls import path, re_path, include
from rest_framework.routers import DefaultRouter
from .Views.auth import (
    LoginView,
    LogoutView,
    RegisterView,
    UserProfileView,
    UserChangePasswordView,
    ResetPasswordView,
)
from .Views.application.applicationView import ApplicationApplyViewSet
from .Views.feedback.feedbackView import FeedbackViewSet
from .Views.internship_submission.internshipSubmissionView import (
    InternshipSubmissionViewSet,
)
from .Views.placement.placementView import PlacementFromApplicationView
from .Views.user_profile.userProfileView import RegisterEditProfileViewSet

app_name = "auth_common"

# Create a router instance
router = DefaultRouter(trailing_slash=False)

# Register your viewsets with the router
router.register(
    r"auth/application-apply", ApplicationApplyViewSet, basename="application-apply"
)
router.register(r"auth/feedback", FeedbackViewSet, basename="feedback")
router.register(
    r"auth/internship-submission",
    InternshipSubmissionViewSet,
    basename="internship-submission",
)
router.register(r"auth/placement", PlacementFromApplicationView, basename="placement")
router.register(
    r"auth/register-profile", RegisterEditProfileViewSet, basename="register-profile"
)

# Define your urlpatterns for views that are not viewsets
urlpatterns = [
    path("auth/login/", LoginView.as_view(), name="login"),
    path("auth/logout/", LogoutView.as_view(), name="logout"),
    path("auth/register/", RegisterView.as_view(), name="register"),
    path("auth/reset-password/", ResetPasswordView.as_view(), name="reset-password"),
    path("auth/user-profile/", UserProfileView.as_view(), name="user-profile"),
    path(
        "auth/change_password/",
        UserChangePasswordView.as_view(),
        name="change-password",
    ),
]

# Include the router URLs
urlpatterns += router.urls
