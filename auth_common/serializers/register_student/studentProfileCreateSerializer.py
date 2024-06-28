from rest_framework import serializers
from auth_common.model.auth.user import User
from auth_common.model.student import Student


class StudentSerializer(serializers.ModelSerializer):
    user = serializers.PrimaryKeyRelatedField(queryset=User.objects.all())

    class Meta:
        model = Student
        fields = "__all__"
