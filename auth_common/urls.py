from django.urls import path, include
from rest_framework.routers import SimpleRouter
from auth_common.Views.application.applicationViewSet import ApplicationViewSet

from auth_common.Views.auth.userCreateView import UserCreateView
from auth_common.Views.organization_registration.organizationRegistrationViewSet import (
    OrganizationRegistrationViewSet,
)
from auth_common.Views.placement.placementView import PlacementView
from auth_common.Views.public_vacancy.publicVacancyViewSet import PublicVacancyView
from auth_common.Views.register_student.studentRegistrationViewSet import (
    StudentRegistrationViewSet,
)
from auth_common.Views.vacancy_post.vacancyPostViewSet import VacancyPostView
from auth_common.Views.auth import (
    LoginView,
    LogoutView,
    UserProfileView,
    UserChangePasswordView,
    ResetPasswordView,
)

app_name = "auth_common"

# Use SimpleRouter instead of DefaultRouter
router = SimpleRouter(trailing_slash=False)

# Register your viewsets with the router
router.register(
    r"student/student-register",
    StudentRegistrationViewSet,
    basename="student-register",
)
router.register(
    r"organization/organization-register",
    OrganizationRegistrationViewSet,
    basename="organization-register",
)
router.register(r"vacancy/vacancy-submit", VacancyPostView, basename="vacancy-submit"),
router.register(
    r"application/apply-application", ApplicationViewSet, basename="apply-application"
),
router.register(r"placement/placement", PlacementView, basename="placement")
router.register(r"vacancy/public-vacancy", PublicVacancyView, basename="public-vacancy")

# Define your urlpatterns for views that are not viewsets
urlpatterns = [
    path("auth/login", LoginView.as_view(), name="login"),
    path("auth/logout", LogoutView.as_view(), name="logout"),
    path("auth/user-create", UserCreateView.as_view(), name="user_create"),
    path("auth/reset-password", ResetPasswordView.as_view(), name="reset-password"),
    path("auth/user-profile", UserProfileView.as_view(), name="user-profile"),
    path(
        "auth/change-password",
        UserChangePasswordView.as_view(),
        name="change-password",
    ),
]

# Include the router URLs
urlpatterns += router.urls
