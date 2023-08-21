from rest_framework import serializers
from ...model.auth import User


class UserBaseCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = [
            "id",
            "email",
            "name",
            "is_student",
            "is_active",
            "is_admin",
            "craeted_at",
            "updated_at",
        ]
