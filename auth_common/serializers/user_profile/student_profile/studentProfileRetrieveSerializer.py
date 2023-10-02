from rest_framework import serializers
from auth_common.model import Student


class StudentProfileRetrieveSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = "__all__"
