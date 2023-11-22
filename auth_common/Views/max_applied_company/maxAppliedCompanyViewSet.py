from rest_framework.response import Response
from rest_framework import viewsets
from rest_framework import status
from django.db.models import Count
from auth_common.model.organization import Organization
from auth_common.serializers.register_organization.organizationSerializer import OrganizationSerializer

class MaxApplicationsOrganizationView(viewsets.ViewSet):
    def list(self, request, *args, **kwargs):
        organization = Organization.objects.annotate(
            max_application_count=Count("vacancies__applications")
        ).order_by("-max_application_count").first()

        if organization:
            serializer = OrganizationSerializer(organization)
            return Response(serializer.data)
        else:
            return Response({"error": "No organizations found"}, status=status.HTTP_404_NOT_FOUND)
