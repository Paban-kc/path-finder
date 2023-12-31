from django.contrib.auth import get_user_model
from django.utils.translation import gettext_lazy as _
from rest_framework import serializers

# get the user model
User = get_user_model()


class UserDetailSerializer(serializers.ModelSerializer):
    """
    User model w/o password
    """

    full_name = serializers.CharField(source="get_full_name", read_only=True)

    @staticmethod
    def validate_username(username):
        return username

    class Meta:
        model = User
        fields = (
            "id",
            "email",
            "is_student"
            "last_name",
            "first_name",
            "full_name",
            "is_superuser",
        )
