from rest_framework import serializers
from auth_common.model import Student

from auth_common.model.auth.user import User
from auth_common.serializers.auth.userProfileSerializer import UserProfileSerializer


class StudentRegisterEditProfileCreateSerializer(serializers.ModelSerializer):
    # user = UserProfileSerializer()

    class Meta:
        model = Student
        exclude = ["user"]

    def create(self, validated_data):
        user = self.context["request"].user
        student = Student.objects.create(user=user, **validated_data)
        return student

    def to_representation(self, instance):
        data = super().to_representation(instance)
        data["first_name"] = instance.user.first_name
        data["last_name"] = instance.user.last_name
        data["email"] = instance.user.email
        data["gender"] = instance.user.gender
        return data
