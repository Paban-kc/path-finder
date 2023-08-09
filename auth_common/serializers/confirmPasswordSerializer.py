# from rest_framework import serializers
# from django.contrib.auth.tokens import default_token_generator
# from django.contrib.auth import get_user_model, password_validation
# from django.contrib.auth.models import AbstractBaseUser

# User = get_user_model()


# class ConfirmPasswordSerializer(serializers.Serializer):
#     token = serializers.CharField()
#     uid = serializers.CharField()
#     new_password1 = serializers.CharField(write_only=True)
#     new_password2 = serializers.CharField(write_only=True)

#     def validate(self, data):
#         token = data.get("token")
#         uid = data.get("uid")

#         try:
#             # Decode the uid to get the user object
#             user = User.objects.get(pk=AbstractBaseUser().id_decoder(uid))
#         except User.DoesNotExist:
#             raise serializers.ValidationError("Invalid uid")

#         # Check if the provided token is valid for the user
#         if not default_token_generator.check_token(user, token):
#             raise serializers.ValidationError("Invalid token")

#         # Validate password
#         new_password1 = data.get("new_password1")
#         new_password2 = data.get("new_password2")
#         if new_password1 != new_password2:
#             raise serializers.ValidationError(
#                 "The two new password fields didn't match."
#             )

#         try:
#             password_validation.validate_password(new_password1, user)
#         except serializers.ValidationError as exc:
#             raise serializers.ValidationError({"new_password1": exc.messages})

#         return data

#     def save(self):
#         token = self.validated_data["token"]
#         uid = self.validated_data["uid"]
#         new_password = self.validated_data["new_password1"]

#         # Implement your password reset confirmation logic here, e.g., set the new password for the user.
#         # You can use the same `UserManager` as in the previous code snippet for the user operations.

#         # For example:
#         try:
#             user = User.objects.get(pk=AbstractBaseUser().id_decoder(uid))
#         except User.DoesNotExist:
#             raise serializers.ValidationError("Invalid uid")

#         user.set_password(new_password)
#         user.save()
