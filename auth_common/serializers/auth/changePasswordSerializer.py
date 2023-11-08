from rest_framework import serializers
from django.contrib.auth.hashers import check_password, make_password

class ChangePasswordSerializer(serializers.Serializer):
    new_password = serializers.CharField(max_length=128, required=True)
    confirm_password = serializers.CharField(max_length=128, required=True)

    def validate(self, data):
        new_password = data.get("new_password")
        confirm_password = data.get("confirm_password")

        if new_password != confirm_password:
            raise serializers.ValidationError("New password and confirm password do not match.")

        return data

    def update_password(self, user):
        new_password = self.validated_data["new_password"]

        if check_password(new_password, user.password):
            raise serializers.ValidationError("New password cannot be the same as the old password.")

        # Hash the new password and save it to the user object
        hashed_password = make_password(new_password)
        user.password = hashed_password
        user.save()
