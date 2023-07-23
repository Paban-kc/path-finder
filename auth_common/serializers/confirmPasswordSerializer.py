from django.conf import settings
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import SetPasswordForm
from django.contrib.auth.tokens import default_token_generator
from django.utils.encoding import force_str
from django.utils.translation import gettext_lazy as _
from rest_framework import serializers
from rest_framework.exceptions import ValidationError

from ..utils import base36_to_int

# Get the UserModel
UserModel = get_user_model()


class ConfirmPasswordSerializer(serializers.Serializer):
    """
    Serializer for confirming a password reset attempt.
    """

    new_password1 = serializers.CharField(
        max_length=128, required=True, allow_blank=False
    )
    new_password2 = serializers.CharField(
        max_length=128, required=True, allow_blank=False
    )
    uid = serializers.CharField(required=True, allow_blank=False)
    token = serializers.CharField(required=True, allow_blank=False)

    set_password_form_class = SetPasswordForm

    _errors = {}
    user = None
    set_password_form = None

    def custom_validation(self, attrs):
        pass

    def validate(self, attrs):
        # Decode the uidb36 to uid to get User object
        try:
            uid = force_str((base36_to_int(attrs["uid"])))
            self.user = UserModel._default_manager.get(pk=uid)
        except (TypeError, ValueError, OverflowError, UserModel.DoesNotExist):
            raise ValidationError({"uid": ["Invalid value"]})

        if not default_token_generator.check_token(self.user, attrs["token"]):
            raise ValidationError({"token": ["Invalid value"]})

        self.custom_validation(attrs)
        # Construct SetPasswordForm instance
        self.set_password_form = self.set_password_form_class(
            user=self.user,
            data=attrs,
        )
        if not self.set_password_form.is_valid():
            raise serializers.ValidationError(self.set_password_form.errors)

        return attrs

    def save(self):
        return self.set_password_form.save()
