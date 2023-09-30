from rest_framework import viewsets
from rest_framework import permissions
from rest_framework.filters import SearchFilter, OrderingFilter
from django_filters.rest_framework import DjangoFilterBackend
from auth_common.model.application import Application
from ...serializers.application import (
    ApplicationApplyCreateSerializer,
    ApplicationListSerializer,
    ApplicationUpdateSerializer,
    ApplicationRetrieveSerializer,
)
from rest_framework import permissions
from rest_framework import viewsets, permissions, status
from rest_framework.response import Response
from rest_framework.exceptions import ValidationError


class ApplicationApplyViewSet(viewsets.ModelViewSet):
    queryset = Application.objects.all()
    serializer_class = ApplicationApplyCreateSerializer
    permission_classes = [permissions.IsAuthenticated]
    lookup_field = "id"
    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
    http_method_names = ["get", "head", "post", "patch", "put", "delete"]
    filterset_fields = [
        "student_profile",
        "internship",
        "status",
        "is_approved",
    ]
    search_fields = [
        "student_profile__user__first_name",
        "student_profile__user__last_name",
        "internship__title",
        "internship__requirements",
    ]

    def perform_create(self, serializer):
        internship_id = self.request.data.get("internship")

        # Check if an application with the same student profile and internship already exists
        existing_application = Application.objects.filter(
            student_profile=self.request.user.student_user, internship_id=internship_id
        ).first()

        if existing_application:
            raise ValidationError("Application already submitted for this internship.")

        serializer.save(
            student_profile=self.request.user.student_user, internship_id=internship_id
        )

    def perform_update(self, serializer):
        instance = serializer.instance
        is_approved = self.request.data.get("is_approved", False)

        if is_approved:
            pass

        instance.is_approved = is_approved
        instance.save()

        serializer.save()

    def get_queryset(self):
        user = self.request.user
        if user.is_superuser or user.is_staff:
            return Application.objects.all()

        elif user.is_organization_user:
            # Filter applications based on the organization user's related objects
            return Application.objects.filter(organization=user.organization_user)
        elif user.is_authenticated and hasattr(user, "student_user"):
            return Application.objects.filter(student_profile=user.student_user)
        else:
            return Application.objects.none()

    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        # Check if the user is allowed to delete this application
        if instance.student_profile.user == request.user:
            self.perform_destroy(instance)
            return Response(status=status.HTTP_204_NO_CONTENT)
        else:
            return Response(
                {"detail": "Permission Denied"}, status=status.HTTP_403_FORBIDDEN
            )

    def get_serializer_class(self):
        if self.action == "list":
            return ApplicationListSerializer
        elif self.action == "retrieve":
            return ApplicationRetrieveSerializer
        elif self.action in ["partial_update", "update"]:
            return ApplicationUpdateSerializer
        else:
            return ApplicationApplyCreateSerializer

    def get_serializer_context(self):
        context = super().get_serializer_context()
        context["student_profile"] = self.request.user.student_user
        return context
