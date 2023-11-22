from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated

from auth_common.serializers.auth.userProfileSerializer import UserProfileSerializer

class UserProfileView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request, format=None):
        user_profile = request.user
        serializer = UserProfileSerializer(user_profile)
        return Response(serializer.data, status=status.HTTP_200_OK)

