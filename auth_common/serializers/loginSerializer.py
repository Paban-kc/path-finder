from django.conf import settings
from django.contrib.auth import authenticate, get_user_model
from django.contrib.auth.forms import PasswordResetForm, SetPasswordForm
from django.urls import exceptions as url_exceptions
from django.utils.encoding import force_str
from django.utils.translation import gettext_lazy as _
from rest_framework import exceptions, serializers
from rest_framework.exceptions import ValidationError

# Get the UserModel
UserModel = get_user_model()


class LoginSerializer(serializers.Serializer):
    email = serializers.EmailField(required=True, allow_blank=False)
    password = serializers.CharField(style={"input_type": "password"})

    def authenticate(self, **kwargs):
        return authenticate(self.context["request"], **kwargs)

    def _validate_email(self, email, password):
        if email and password:
            user = self.authenticate(email=email, password=password)
        else:
            msg = _('Must include "email" and "password".')
            raise ValidationError(msg)

        return user

    @staticmethod
    def validate_auth_user_status(user):
        if not user.is_active:
            msg = _("User account is disabled.")
            raise ValidationError(msg)

    def validate(self, attrs):
        email = attrs.get("email")
        password = attrs.get("password")
        user = self._validate_email(email, password)

        if not user:
            msg = _("Unable to log in with provided credentials.")
            raise ValidationError(msg)

        # Did we get back an active user?
        self.validate_auth_user_status(user)

        attrs["user"] = user
        return attrs
