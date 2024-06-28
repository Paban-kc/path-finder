from rest_framework import status
from rest_framework.generics import CreateAPIView
from rest_framework.response import Response
from auth_common.Views.auth.get_token import get_tokens_for_user
from ...serializers.auth.userCreateSerializer import UserCreateSerializer


class UserCreateView(CreateAPIView):
    serializer_class = UserCreateSerializer

    def post(self, request, format=None):
        serializer = UserCreateSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            user = serializer.save()
            token = get_tokens_for_user(user)
            user_id = user.id
            return Response(
                {
                    "user_id": user_id,
                    "Token": token,
                    "msg": "user created successfully",
                },
                status=status.HTTP_201_CREATED,
            )
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
