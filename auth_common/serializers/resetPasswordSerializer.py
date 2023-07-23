from django.conf import settings
from django.contrib.auth import get_user_model
from django.contrib.auth.tokens import default_token_generator
from django.urls import reverse
from django.utils.translation import gettext as _
from rest_framework import serializers

from ..utils import int_to_base36, send_mail

UserModel = get_user_model()


class ResetPasswordSerializer(serializers.Serializer):
    """
    Serializer for requesting a password reset e-mail.
    """

    email = serializers.EmailField(required=True, allow_blank=False)

    def validate_email(self, value):
        if not UserModel.objects.filter(username=value).exists():
            raise serializers.ValidationError(_("User does not exists."))
        return value

    def save(self, **kwargs):
        email = self.validated_data["email"]
        token_generator = kwargs.get("token_generator", default_token_generator)
        request = self.context.get("request")

        for user in self.users:
            token = token_generator.make_token(user)

            path = reverse(
                "confirm_password_template",
                args=[int_to_base36(user.pk), token],
            )
            url = request.build_absolute_uri(path)

            context = {"User": user, "reset_password_url": url, "request": request}
            send_mail(settings.MAIL_NAME["RESET_PASSWORD"], [user.id], **context)
        return email
