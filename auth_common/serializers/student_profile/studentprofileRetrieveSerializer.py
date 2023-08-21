from rest_framework import serializers
from ...model import StudentProfile
from ..auth import UserBaseCreateSerializer


class StudentRetrieveSerializer(UserBaseCreateSerializer):
    class Meta:
        model = StudentProfile
        fields = "__all__"
