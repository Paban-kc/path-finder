from ...model.auth import User

from rest_framework import serializers


class UserProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = [
            "id",
            "email",
            "name",
            "is_student",
            "is_active",
            "is_admin",
        ]
