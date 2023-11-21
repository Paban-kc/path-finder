from rest_framework import serializers
from auth_common.model import Student
from auth_common.model.auth.user import User
from auth_common.serializers.auth.userBaseSerializer import UserSerializer


class StudentSerializer(serializers.ModelSerializer):
    user = serializers.PrimaryKeyRelatedField(queryset=User.objects.all())

    class Meta:
        model = Student
        fields = '__all__'
