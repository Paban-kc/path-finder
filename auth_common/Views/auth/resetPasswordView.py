from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from ...serializers.auth import ResetPasswordSerializer


class ResetPasswordView(APIView):
    def post(self, request, format=None):
        serializer = ResetPasswordSerializer(
            data=request.data, context={"request": request}
        )
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(
            {"message": "Password reset successful"}, status=status.HTTP_200_OK
        )
