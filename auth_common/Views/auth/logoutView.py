from django.contrib.auth import logout
from rest_framework import status
from rest_framework.generics import GenericAPIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework import serializers  # Import the serializer module


class LogoutView(GenericAPIView):
    """
    Calls Django logout method to logout the current session.
    Accepts/Returns nothing.
    """

    permission_classes = (IsAuthenticated,)
    throttle_scope = "auth"
    swagger_fake_view = True

    # def get_serializer_class(self):
    #     # Use the generic Serializer class
    #     return serializers.Serializer

    def post(self, request):
        logout(request)
        return Response({"msg": "Logout success"}, status=status.HTTP_200_OK)
