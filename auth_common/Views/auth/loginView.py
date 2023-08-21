from django.contrib.auth import login as django_login
from django.contrib.auth import logout as django_logout
from django.utils.translation import gettext_lazy as _
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from ...serializers.auth import LoginSerializer
from django.contrib.auth import authenticate
from .registerView import get_tokens_for_user

class LoginView(APIView):
    def post(self, request, format=None):
        serializer = LoginSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            email = serializer.data.get("email")
            password = serializer.data.get("password")
            user = authenticate(email=email, password=password)
            if user is not None:
                token = get_tokens_for_user(user)
                return Response({"Token":token,"msg": "Login success"}, status=status.HTTP_200_OK)

            else:
                return Response(
                    {"errors": {"non_field_errors": ["Email or Password i not valid"]}},
                    status=status.HTTP_404_NOT_FOUND,
                )

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
