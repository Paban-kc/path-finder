from rest_framework import status
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from auth_common.model.organization import Organization
from auth_common.serializers.register_organization.organizationSerializer import (
    OrganizationSerializer,
)
from rest_framework import viewsets
from rest_framework import status
from rest_framework.response import Response


class OrganizationRegistrationViewSet(viewsets.ModelViewSet):
    serializer_class = OrganizationSerializer
    queryset = Organization.objects.all()

    def post(self, request, *args, **kwargs):
        user = request.data.get("user")
        org_serializer = OrganizationSerializer(data=request.data)

        if org_serializer.is_valid(raise_exception=True):
            org_serializer.save()

            return Response(
                status=status.HTTP_201_CREATED,
            )
        return Response(
            {"msg": "Organization registration failed"},
            status=status.HTTP_400_BAD_REQUEST,
        )
