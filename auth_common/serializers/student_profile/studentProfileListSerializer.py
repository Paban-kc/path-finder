from rest_framework import serializers
from ...model import StudentProfile
from ..auth import UserBaseCreateSerializer


class StudentListSerializer(UserBaseCreateSerializer):
    class Meta:
        model = StudentProfile
        fields = "__all__"
