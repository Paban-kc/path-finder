from auth_common.model.organization import Organization
from ...model.auth import User

from rest_framework import serializers


class UserProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = [
            "id",
            "email",
            "first_name",
            "last_name",
            "gender",
            "is_student",
            "is_active",
            "is_admin",
        ]
