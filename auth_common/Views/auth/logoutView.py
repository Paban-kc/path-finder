from django.contrib.auth import logout
from rest_framework import status
from rest_framework.generics import GenericAPIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response


class LogoutView(GenericAPIView):
    """
    Calls Django logout mehtod to logout current session.
    Accepts/Returns nothing.
    """

    permission_classes = (IsAuthenticated,)
    throttle_scope = "auth"

    def post(self, request):
        logout(request)
        return Response(status=status.HTTP_204_NO_CONTENT)
