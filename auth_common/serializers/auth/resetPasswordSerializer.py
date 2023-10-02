from django.conf import settings
from django.contrib.auth import get_user_model, update_session_auth_hash
from django.contrib.auth.tokens import default_token_generator
from django.utils.translation import gettext as _
from rest_framework import serializers
from django.contrib.auth.forms import SetPasswordForm
from django.core.mail import send_mail

UserModel = get_user_model()


class ResetPasswordSerializer(serializers.Serializer):
    old_password = serializers.CharField(max_length=128)
    new_password1 = serializers.CharField(max_length=128)
    new_password2 = serializers.CharField(max_length=128)

    set_password_form_class = SetPasswordForm

    set_password_form = None

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.request = self.context.get("request")
        self.user = getattr(self.request, "user", None)

    def validate_old_password(self, value):
        if not self.user.check_password(value):
            err_msg = _("Your old password was entered incorrectly. Please enter it again.")
            raise serializers.ValidationError(err_msg)
        return value


    def custom_validation(self, attrs):
        pass

    def validate(self, attrs):
        self.set_password_form = self.set_password_form_class(
            user=self.user,
            data=attrs,
        )

        self.custom_validation(attrs)
        if not self.set_password_form.is_valid():
            raise serializers.ValidationError(self.set_password_form.errors)

        # Check if new password is the same as the old password
        new_password = attrs.get("new_password1")
        if self.user.check_password(new_password):
            raise serializers.ValidationError(
                "New password must be different from old password."
            )

        # Update attrs dictionary with cleaned data
        attrs["new_password1"] = self.set_password_form.cleaned_data["new_password1"]
        return attrs

    def save(self):
        self.set_password_form.save()
        update_session_auth_hash(self.request, self.user)
        # Send email after resetting the password
        subject = 'Password Reset Successful'
        message = 'Your password has been successfully reset.'
        from_email = settings.DEFAULT_FROM_EMAIL
        recipient_list = [self.user.email]

        send_mail(subject, message, from_email, recipient_list)
