from rest_framework.response import Response
from rest_framework import viewsets
from rest_framework import status
from django.db.models import Count
from auth_common.model.organization import Organization
from auth_common.model.vacancy import Vacancy
from auth_common.serializers.register_organization.organizationSerializer import (
    OrganizationSerializer,
)
from auth_common.serializers.vacancy.vacancyListSerializer import VacancyListSerializer


class MaxApplicationsOrganizationView(viewsets.ViewSet):
    def list(self, request, *args, **kwargs):
        vacancies = Vacancy.objects.annotate(
            application_count=Count("applications")
        ).order_by("-application_count")

        if vacancies.exists():
            # Serialize the vacancies with application counts
            serializer = VacancyListSerializer(vacancies, many=True)
            return Response(serializer.data)
        else:
            return Response({"error": "No vacancies found"}, status=status.HTTP_404_NOT_FOUND)