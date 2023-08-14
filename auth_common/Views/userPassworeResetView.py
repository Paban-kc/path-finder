from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from ..serializers.userPasswordResetSerializer import UserPasswordResetSerializer


class UserPasswordResetView(APIView):
    def post(self, request, uid, token, format=None):
        serializer = UserPasswordResetSerializer(
            data=request.data, context={"uid": uid, "token": token}
        )
        if serializer.is_valid(raise_exception=True):
            return Response(
                {"msh": "Password Reset successfully"}, status=status.HTTP_200_OK
            )

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
