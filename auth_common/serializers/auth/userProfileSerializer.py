from rest_framework import serializers
from auth_common.model.auth.user import User
from auth_common.model.student import Student
from auth_common.model.organization import Organization

from auth_common.serializers.register_student.studentProfileCreateSerializer import (
    StudentSerializer,
)


class OrganizationSerializer(serializers.ModelSerializer):
    user = serializers.PrimaryKeyRelatedField(queryset=User.objects.all())

    class Meta:
        model = Organization
        fields = "__all__"


class UserProfileSerializer(serializers.Serializer):
    # user_type = serializers.CharField(source='get_user_type_display', read_only=True)
    student_profile = StudentSerializer(source="student_user", read_only=True)
    # organization_profile = OrganizationSerializer(
    #     source="organization_user", read_only=True
    # )
    is_student = serializers.SerializerMethodField(source="get_is_student")

    class Meta:
        model = User
        fields = ("user_type", "student_profile", "organization_profile", "is_student")

    def get_is_student(self, instance):
        try:
            student_instance = Student.objects.get(user=instance)
            return True
        except Student.DoesNotExist as e:
            return False
