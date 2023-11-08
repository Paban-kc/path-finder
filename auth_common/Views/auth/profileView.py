from rest_framework.views import APIView
from ...serializers.auth import UserProfileSerializer
from rest_framework import status
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated


class UserProfileView(APIView):
    permission_classes = [
        IsAuthenticated
    ]  

    def get(self, request, format=None):
        user = request.user
        serializer = UserProfileSerializer(user)
        return Response(serializer.data, status=status.HTTP_200_OK)
