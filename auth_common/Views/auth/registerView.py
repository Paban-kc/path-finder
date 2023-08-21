from rest_framework import status
from rest_framework.generics import CreateAPIView
from rest_framework.response import Response
from ...serializers.auth import RegisterSerializer
from rest_framework_simplejwt.tokens import RefreshToken


def get_tokens_for_user(user):
    refresh = RefreshToken.for_user(user)

    return {
        "refresh": str(refresh),
        "access": str(refresh.access_token),
    }


class RegisterView(CreateAPIView):
    serializer_class = RegisterSerializer

    def post(self, request, format=None):
        print("Request Data:", request.data)
        serializer = RegisterSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            print("Serialized Data:", serializer.validated_data)
            user = serializer.save()
            token = get_tokens_for_user(user)
            return Response(
                {"token": token, "msg": "Registration in success"},
                status=status.HTTP_201_CREATED,
            )
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
