from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from ..serializers import ChangePasswordSerializer
from rest_framework import status
from rest_framework.response import Response


class UserChangePasswordView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request, format=None):
        serializer = ChangePasswordSerializer(
            data=request.data, context={"request": request}
        )

        if serializer.is_valid(raise_exception=True):
            return Response(
                {"msg": "Password changed successfully"}, status=status.HTTP_200_OK
            )
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
