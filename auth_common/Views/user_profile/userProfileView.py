from django.shortcuts import render, redirect
from rest_framework import viewsets
from rest_framework.response import Response
from ...serializers.user_profile import (
    OrganizationProfileCreateSerializer,
    StudentProfileCreateSerializer,
)
from django.http import QueryDict
from rest_framework import status
from rest_framework.filters import SearchFilter, OrderingFilter
from django_filters import rest_framework as filters
from rest_framework.filters import OrderingFilter, SearchFilter
from rest_framework import status
from rest_framework.decorators import action

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

from ...model.organization import Organization
from ...model.student import Student

# from .filters.filterForOrganizationProfile import FilterForOrganization
# from .filters.filterForStudentProfile import FilterForStudent


class RegisterEditProfileViewSet(viewsets.ModelViewSet):
    filter_backends = [filters.DjangoFilterBackend, OrderingFilter, SearchFilter]
    http_method_names = ["get", "head", "post", "patch", "put"]
    # filterset_class = {"list": FilterForStudent, "list_profile": FilterForOrganization}

    def get_queryset(self):
        user = self.request.user
        if user.is_student:
            return Student.objects.filter(user=user)
        return Organization.objects.filter(user=user)

    def registration_view(self, data):
        user = self.request.user
        is_student = user.is_student

        # Create a mutable copy of the data
        mutable_data = QueryDict(mutable=True)
        mutable_data.update(data)

        if is_student:
            mutable_data["user[email]"] = user.email
            mutable_data["user[first_name]"] = user.first_name
            mutable_data["user[last_name]"] = user.last_name
            mutable_data["user[gender]"] = user.gender
            mutable_data["user[is_student]"] = user.is_student
            serializer = StudentProfileCreateSerializer(
                data=mutable_data, context={"request": self.request}
            )
        else:
            mutable_data["user[email]"] = user.email
            mutable_data["user[first_name]"] = user.first_name
            serializer = OrganizationProfileCreateSerializer(
                data=mutable_data, context={"request": self.request}
            )

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    @action(detail=False, methods=["post"])
    def create_profile(self, request):
        return self.registration_view(request.data)

    @action(detail=True, methods=["get"])
    def retrieve_profile(self, request, pk=None):
        profile = self.get_object(pk)
        if profile is None:
            return Response(
                {"detail": "Profile not found."}, status=status.HTTP_404_NOT_FOUND
            )

        if profile.user.is_student:
            serializer = StudentProfileRetrieveSerializer(profile)
        else:
            serializer = OrganizationProfileRetrieveSerializer(profile)

        return Response(serializer.data, status=status.HTTP_200_OK)

    def partial_update(self, request, *args, **kwargs):
        user = self.request.user
        is_student = user.is_student

        if is_student:
            instance = user.student_user
            serializer = StudentProfileUpdateSerializer(
                instance, data=request.data, partial=True
            )
        else:
            instance = user.organization_user
            serializer = OrganizationProfileUpdateSerializer(
                instance, data=request.data, partial=True
            )

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    @action(detail=True, methods=["put", "patch"])
    def update_profile(self, request, pk=None):
        profile = self.get_object(pk)
        if profile is None:
            return Response(
                {"detail": "Profile not found."}, status=status.HTTP_404_NOT_FOUND
            )

        if profile.user.is_student:
            serializer = StudentProfileUpdateSerializer(profile, data=request.data)
        else:
            serializer = OrganizationProfileUpdateSerializer(profile, data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def list(self, request):
        user = request.user
        is_student = user.is_student

        if is_student:
            profiles = Student.objects.filter(user=user)
            serializer = StudentProfileListSerializer(profiles, many=True)
        else:
            profiles = Organization.objects.filter(user=user)
            serializer = OrganizationProfileListSerializer(profiles, many=True)

        return Response(serializer.data, status=status.HTTP_200_OK)

    def list_profiles(self, request):
        user = request.user
        if user.is_student:
            profiles = Student.objects.filter(user=user)
            serializer = StudentProfileListSerializer(profiles, many=True)
        else:
            profiles = Organization.objects.filter(user=user)
            serializer = OrganizationProfileListSerializer(profiles, many=True)

        return Response(serializer.data, status=status.HTTP_200_OK)

    def create(self, request, *args, **kwargs):
        return self.registration_view(request.data)
