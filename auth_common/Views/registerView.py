from django.contrib.auth import login
from django.utils.decorators import method_decorator
from django.utils.translation import gettext_lazy as _
from django.views.decorators.debug import sensitive_post_parameters
from rest_framework import status
from rest_framework.generics import CreateAPIView
from rest_framework.permissions import AllowAny
from rest_framework.response import Response

from ..serializers import JWTSerializer, RegisterSerializer
from ..utils.jwtEncode import jwt_encode

sensitive_post_parameters_m = method_decorator(
    sensitive_post_parameters("password1", "password2"),
)


class RegisterView(CreateAPIView):
    serializer_class = RegisterSerializer
    permission_classes = (AllowAny,)
    throttle_scope = "auth"

    @sensitive_post_parameters_m
    def dispatch(self, *args, **kwargs):
        return super().dispatch(*args, **kwargs)

    def get_response_data(self, user):
        token = jwt_encode(user)
        data = {
            "token": token,
        }
        return JWTSerializer(data, context=self.get_serializer_context()).data

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        data = self.get_response_data(user)

        response = Response(
            data,
            status=status.HTTP_201_CREATED,
            headers=headers,
        )

        return response

    def perform_create(self, serializer):
        user = serializer.save(self.request)
        login(self.request, user)
        return user
