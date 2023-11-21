from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from rest_framework import status
from rest_framework.response import Response

from auth_common.serializers.auth.changePasswordSerializer import (
    ChangePasswordSerializer,
)


class UserChangePasswordView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request, format=None):
        serializer = ChangePasswordSerializer(data=request.data)

        if serializer.is_valid(raise_exception=True):
            serializer.update_password(request.user)
            return Response(
                {"msg": "Password changed successfully"}, status=status.HTTP_200_OK
            )
