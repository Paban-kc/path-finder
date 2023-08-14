# from rest_framework.views import APIView
# from ..serializers import SendPasswordResetEmailSerializer
# from rest_framework import status
# from rest_framework.response import Response


# class SendPasswordResetEmailView(APIView):
#     def post(self, request, format=None):
#         serializer = SendPasswordResetEmailSerializer(data=request.data)
#         if serializer.is_valid(raise_exception=True):
#             return Response(
#                 {"msg": "Password reset link send, please check your email"}, status=status.HTTP_200_OK
#             )
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
