from rest_framework.views import APIView
from ..serializers.userProfileSerializer import UserProfileSerializer
from rest_framework import status
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated


class UserProfileView(APIView):
    permission_classes = [
        IsAuthenticated
    ]  

    def get(self, request, format=None):
        user = request.user  # Get the authenticated user
        serializer = UserProfileSerializer(user)  # Pass the user to the serializer
        return Response(serializer.data, status=status.HTTP_200_OK)
