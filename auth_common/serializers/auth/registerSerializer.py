from django.contrib.auth import get_user_model
from rest_framework import serializers

User = get_user_model()


class RegisterSerializer(serializers.ModelSerializer):
    password2 = serializers.CharField(style={"input_type": "password"}, write_only=True)

    class Meta:
        model = User
        fields = ["first_name","last_name","gender", "email", "is_student", "password", "password2"]
        extra_kwargs = {"password": {"write_only": True}}


    def validate(self, attrs):
        password = attrs.get("password")
        password2 = attrs.get("password2")

        if password != password2:
            raise serializers.ValidationError(
                "password and confirm password do not match"
            )
        return attrs

    def create(self, validated_data):
        is_student = validated_data.pop(
            "is_student"
        )  # Remove is_student from validated_data
        return User.objects.create_user(is_student=is_student, **validated_data)
