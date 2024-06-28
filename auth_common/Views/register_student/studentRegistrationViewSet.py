from rest_framework import status
from rest_framework.response import Response

from rest_framework.permissions import IsAuthenticated
from auth_common.model.student import Student
from rest_framework import viewsets
from auth_common.serializers.register_student.studentProfileCreateSerializer import (
    StudentSerializer,
)


class StudentRegistrationViewSet(viewsets.ModelViewSet):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer
    permission_classes = [IsAuthenticated]

    def post(self, request, *args, **kwargs):
        user = request.data.get("user")
        org_serializer = StudentSerializer(data=request.data)

        if org_serializer.is_valid(raise_exception=True):
            org_serializer.save()

            return Response(
                status=status.HTTP_201_CREATED,
            )
        return Response(
            {"msg": "Student registration failed"},
            status=status.HTTP_400_BAD_REQUEST,
        )
