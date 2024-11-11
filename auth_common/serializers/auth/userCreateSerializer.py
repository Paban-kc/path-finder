from django.contrib.auth import get_user_model
from rest_framework import serializers
from django.core.mail import send_mail
from django.conf import settings

User = get_user_model()

class UserCreateSerializer(serializers.ModelSerializer):
    confirm_password = serializers.CharField(
        style={"input_type": "password"}, write_only=True
    )

    class Meta:
        model = User
        fields = ["email", "password", "confirm_password", "first_name", "last_name"]
        extra_kwargs = {"password": {"write_only": True}}

    def validate(self, attrs):
        password = attrs.get("password")
        confirm_password = attrs.get("confirm_password")

        if password != confirm_password:
            raise serializers.ValidationError(
                "Password and confirm password do not match"
            )
        return attrs

    def create(self, validated_data):
        validated_data.pop("confirm_password", None)
        user = User.objects.create_user(**validated_data)

        # Send email notification after successful registration
        subject = "Welcome to Path Finder"
        message = "Thank you for registering with Path Finder. Welcome aboard!"
        from_email = settings.DEFAULT_FROM_EMAIL
        recipient_list = [user.email]

        send_mail(subject, message, from_email, recipient_list)

        return user
