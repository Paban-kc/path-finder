from django.utils.translation import gettext_lazy as _
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from ...serializers.auth import LoginSerializer
from django.contrib.auth import authenticate
from .userCreateView import get_tokens_for_user


class LoginView(APIView):
    def post(self, request, format=None):
        serializer = LoginSerializer(data=request.data)

        if serializer.is_valid(raise_exception=True):
            email = serializer.data.get("email")
            password = serializer.data.get("password")
            user = authenticate(email=email, password=password)

            if user is not None:
                token = get_tokens_for_user(user)

                # Check logedin user is a Student or an Organization
                if hasattr(user, "student_user"):
                    student_id = user.student_user.id
                    return Response(
                        {
                            "Token": token,
                            "msg": "Login success",
                            "Student_id": student_id,
                        },
                        status=status.HTTP_200_OK,
                    )
                elif hasattr(user, "organization_user"):
                    organization_id = user.organization_user.id
                    return Response(
                        {
                            "Token": token,
                            "msg": "Login success",
                            "organization_id": organization_id,
                        },
                        status=status.HTTP_200_OK,
                    )
                else:
                    return Response(
                        {"errors": {"non_field_errors": ["User type not recognized"]}},
                        status=status.HTTP_401_UNAUTHORIZED,
                    )

        return Response(
            {"errors": {"non_field_errors": ["Invalid email or password"]}},
            status=status.HTTP_401_UNAUTHORIZED,
        )
