from rest_framework import viewsets
from rest_framework.response import Response

from rest_framework.permissions import IsAuthenticated
from rest_framework import status
from rest_framework.filters import SearchFilter, OrderingFilter
from django_filters import rest_framework as filters
from rest_framework.filters import OrderingFilter, SearchFilter
from rest_framework import status

from ...serializers.user_profile.organization_profile import (
    OrganizationProfileCreateSerializer,
    OrganizationProfileListSerializer,
    OrganizationProfileRetrieveSerializer,
    OrganizationProfileUpdateSerializer,
)
from ...serializers.user_profile.student_profile import (
    StudentProfileCreateSerializer,
    StudentProfileListSerializer,
    StudentProfileRetrieveSerializer,
    StudentProfileUpdateSerializer,
)
from rest_framework import viewsets

from ...model.organization import Organization
from ...model.student import Student


class RegisterEditProfileViewSet(viewsets.ModelViewSet):
    filter_backends = [filters.DjangoFilterBackend, OrderingFilter, SearchFilter]
    serializer_class = StudentProfileCreateSerializer
    http_method_names = ["get", "head", "post", "patch", "put"]
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        user = self.request.user
        if user.is_student:
            return Student.objects.filter(user=user)
        return Organization.objects.filter(user=user)

    def create(self, request, *args, **kwargs):
        user = self.request.user
        is_student = user.is_student
        mutable_data = request.data.copy()
        mutable_data["user[email]"] = user.email
        mutable_data["user[first_name]"] = user.first_name
        mutable_data["user[last_name]"] = user.last_name
        mutable_data["user[gender]"] = user.gender
        mutable_data["user[is_student]"] = user.is_student

        if is_student:
            serializer = StudentProfileCreateSerializer(
                data=mutable_data, context={"request": self.request}
            )
        else:
            serializer = OrganizationProfileCreateSerializer(
                data=mutable_data, context={"request": self.request}
            )

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def retrieve(self, request, *args, **kwargs):
        instance = self.get_object()
        if instance is None:
            return Response(
                {"detail": "Profile not found."}, status=status.HTTP_404_NOT_FOUND
            )
        if instance.user.is_student:

            serializer = StudentProfileRetrieveSerializer(instance)
        else:
            serializer = OrganizationProfileRetrieveSerializer(instance)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def update(self, request, *args, **kwargs):
        instance = self.get_object()
        if instance is None:
            return Response(
                {"detail": "Profile not found."}, status=status.HTTP_404_NOT_FOUND
            )
        if instance.user.is_student:
            serializer = StudentProfileUpdateSerializer(
                instance, data=request.data, partial=True
            )
        else:
            serializer = OrganizationProfileUpdateSerializer(
                instance, data=request.data, partial=True
            )
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def list(self, request, *args, **kwargs):
        user = request.user
        is_student = user.is_student
        if is_student:
            profiles = Student.objects.filter(user=user)
            serializer = StudentProfileListSerializer(profiles, many=True)
        else:
            profiles = Organization.objects.filter(user=user)
            serializer = OrganizationProfileListSerializer(profiles, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
