from django.shortcuts import render, redirect
from rest_framework import viewsets
from rest_framework.response import Response
from ...serializers.register_edit_profile import (
    OrganizationRegisterEditProfileCreateSerializer,
    StudentRegisterEditProfileCreateSerializer,
)
from rest_framework import status


class RegisterEditProfileViewSet(viewsets.ViewSet):
    def registration_view(self, data):
        user = self.request.user
        is_student = user.is_student

        if is_student:
            data["user"] = {
                "email": user.email,
                "first_name": user.first_name,
                "last_name": user.last_name,
                "gender": user.gender,
                "is_student": user.is_student,
            }
            serializer = StudentRegisterEditProfileCreateSerializer(
                data=data, context={"request": self.request}
            )
        else:
            data["user"] = {
                "email": user.email,
                "first_name": user.first_name,
                "last_name": user.last_name,
                "gender": user.gender,
                "is_student": user.is_student,
            }
            serializer = StudentRegisterEditProfileCreateSerializer(
                data=data, context={"request": self.request}
            )
            serializer = OrganizationRegisterEditProfileCreateSerializer(
                data=data, context={"request": self.request}
            )


        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def create(self, request, *args, **kwargs):
        return self.registration_view(request.data)

    def list(self, request, *args, **kwargs):
        return Response(
            {"detail": "This endpoint does not support list action."},
            status=status.HTTP_405_METHOD_NOT_ALLOWED,
        )
