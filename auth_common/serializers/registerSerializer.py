from django.contrib.auth import get_user_model
from django.contrib.auth.password_validation import validate_password
from django.core.exceptions import ValidationError as DjangoValidationError
from django.utils.translation import gettext_lazy as _
from rest_framework import serializers

User = get_user_model()


class RegisterSerializer(serializers.Serializer):
    email = serializers.EmailField(required=True)
    password1 = serializers.CharField(write_only=True)
    password2 = serializers.CharField(write_only=True)

    first_name = serializers.CharField(max_length=150, required=True)
    last_name = serializers.CharField(max_length=150, required=True)

    def validate_email(self, email):
        if User.objects.filter(email=email).exists():
            raise serializers.ValidationError("already_exist")
        return email

    def validate_password1(self, password):
        return validate_password(password)

    def validate(self, data):
        if data["password1"] != data["password2"]:
            raise serializers.ValidationError(
                _("The two password fields didn't match.")
            )
        return data

    def save(self, request):
        user = User()
        user.email = self.validated_data["email"]
        user.set_password(self.validated_data["password1"])

        try:
            validate_password(self.validated_data["password1"], user=user)
        except DjangoValidationError as exc:
            raise serializers.ValidationError(
                detail=serializers.as_serializer_error(exc)
            )
        self.set_user_extend_fields(
            user,
        )
        user.save()
        return user

    def set_user_extend_fields(self, user):
        setattr(user, "first_name", self.validated_data["first_name"])
        setattr(user, "last_name", self.validated_data["last_name"])
