from rest_framework import viewsets
from rest_framework.filters import OrderingFilter, SearchFilter
from django_filters import rest_framework as filters
from ...model.student import StudentProfile
from ...serializers.student_profile import (
    StudentCreateSerializer,
    StudentListSerializer,
    StudentRetrieveSerializer,
    StudentUpdateSerializer,
)
from rest_framework.response import Response


class StudentProfileViewSet(viewsets.ModelViewSet):
    filter_backends = [filters.DjangoFilterBackend, OrderingFilter, SearchFilter]
    serializer_class = StudentCreateSerializer
    queryset = StudentProfile.objects.all()

    def get_serializer_class(self):
        if self.action == "list":
            return StudentListSerializer
        elif self.action == "retrieve":
            return StudentRetrieveSerializer
        elif self.action in ("update", "partial_update"):
            return StudentUpdateSerializer
        return StudentCreateSerializer

    def perform_create(self, serializer):
        serializer.save()

    def perform_update(self, serializer):
        serializer.save()

    def perform_destroy(self, instance):
        instance.delete()
