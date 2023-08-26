from django.contrib.auth import update_session_auth_hash
from django.contrib.auth.forms import SetPasswordForm
from django.utils.translation import gettext_lazy as _
from rest_framework import serializers


class ChangePasswordSerializer(serializers.Serializer):
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
        invalid_password_conditions = (
            self.user,
            not self.user.check_password(value),
        )

        if all(invalid_password_conditions):
            err_msg = _(
                "Your old password was entered incorrectly. Please enter it again."
            )
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
        return attrs


    def save(self):
        self.set_password_form.save()
        update_session_auth_hash(self.request, self.user)
        
