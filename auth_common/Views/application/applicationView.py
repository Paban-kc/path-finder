from rest_framework import viewsets
from auth_common.model.application import Application
from auth_common.serializers.application.applicationCreateSerializer import (
    ApplicationApplyCreateSerializer,
)
from auth_common.serializers.application.applicationListSerailizer import (
    ApplicationListSerializer,
)
from auth_common.serializers.application.applicationUpdateSerializer import (
    ApplicationUpdateSerializer,
)
from auth_common.serializers.application.applicationRetrieveSerializer import (
    ApplicationRetrieveSerializer,
)
from rest_framework.filters import SearchFilter, OrderingFilter
from django_filters.rest_framework import DjangoFilterBackend
from auth_common.serializers.user_profile.student_profile.studentProfileListSerializer import StudentProfileListSerializer


class ApplicationApplyViewSet(viewsets.ModelViewSet):
    queryset = Application.objects.all()
    serializer_class = ApplicationApplyCreateSerializer
    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]

    filterset_fields = ["student_profile", "internship", "status"]
    search_fields = [
        "student_profile__user__first_name",
        "student_profile__user__last_name",
        "internship__title",
    ]
    ordering_fields = ["date_applied", "status"]
    http_method_names = ["get", "head", "post", "patch", "put", "delete"]

    def perform_create(self, serializer):
        student = self.request.user.student_user
        internship_id = self.request.data.get("internship")
        serializer.save(student_profile=student, internship_id=internship_id)

    def get_serializer_class(self):
        if self.action == "create":
            return ApplicationApplyCreateSerializer
        elif self.action == "list":
            return ApplicationListSerializer
        elif self.action == "retrieve":
            return ApplicationRetrieveSerializer
        elif self.action == "partial_update":
            return ApplicationUpdateSerializer
        else:
            return super().get_serializer_class()

    def perform_create(self, serializer):
        student = self.request.user.student_user
        internship_id = self.request.data.get("internship")
        serializer.save(student_profile=student, internship_id=internship_id)

    def get_serializer_context(self):
        context = super().get_serializer_context()
        student = self.request.user.student_user
        context["student_profile"] = StudentProfileListSerializer(student).data
        return context
