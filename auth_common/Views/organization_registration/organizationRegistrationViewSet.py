from rest_framework import viewsets
from rest_framework import status
from rest_framework.response import Response
from auth_common.model.organization import Organization
from auth_common.serializers.auth.userProfileSerializer import OrganizationSerializer
from auth_common.serializers.register_organization.organizationListSerializer import (
    OrganizationListSerializer,
)


class OrganizationRegistrationViewSet(viewsets.ModelViewSet):
    serializer_class = OrganizationSerializer
    queryset = Organization.objects.all()

    def get_serializer_class(self):
        if self.request.method == "POST":
            return OrganizationSerializer
        elif self.request.method == "GET":
            return OrganizationListSerializer
        return OrganizationSerializer

    def list(self, request, *args, **kwargs):
        serializer_class = self.get_serializer_class()
        queryset = self.filter_queryset(self.get_queryset())
        serializer = serializer_class(queryset, many=True)
        return Response(serializer.data)

    def create(self, request, *args, **kwargs):
        user = request.data.get("user")
        org_serializer = self.get_serializer(data=request.data)

        if org_serializer.is_valid(raise_exception=True):
            org_instance = org_serializer.save()

            # Assuming user is a ForeignKey in the Organization model
            organization_id = org_instance.id

            return Response(
                {
                    "organization_id": organization_id,
                    "msg": "Organization registration created successfully"
                    
                },
                status=status.HTTP_201_CREATED,
            )
        return Response(
            {"msg": "Organization registration failed"},
            status=status.HTTP_400_BAD_REQUEST,
        )
