from rest_framework import status
from rest_framework.generics import CreateAPIView
from rest_framework.response import Response
from ..serializers import RegisterSerializer
from ..serializers import RegisterSerializer


class RegisterView(CreateAPIView):
    serializer_class = RegisterSerializer

    def post(self, request, format=None):
        serailizer = RegisterSerializer(data=request.data)
        if serailizer.is_valid(raise_exception=True):
            user = serailizer.save()
            return Response(
                {"msg": "Registration in success"}, status=status.HTTP_201_CREATED
            )
        return Response(serailizer.errors, status=status.HTTP_400_BAD_REQUEST)
