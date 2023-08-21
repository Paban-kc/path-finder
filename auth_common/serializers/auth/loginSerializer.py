from django.conf import settings
from django.contrib.auth import authenticate, get_user_model
from django.contrib.auth.forms import PasswordResetForm, SetPasswordForm
from django.urls import exceptions as url_exceptions
from django.utils.encoding import force_str
from django.utils.translation import gettext_lazy as _
from rest_framework import exceptions, serializers
from rest_framework.exceptions import ValidationError
from ...model.auth import User


class LoginSerializer(serializers.ModelSerializer):
   email= serializers.CharField(max_length=255 )
   class Meta:
      model=User
      fields=["email","password"]