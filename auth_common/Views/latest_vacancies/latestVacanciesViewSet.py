from rest_framework.response import Response
from rest_framework import viewsets
from rest_framework import status

from auth_common.model.vacancy import Vacancy
from auth_common.serializers.vacancy.vacancyListSerializer import VacancyListSerializer


class LatestVacanciesView(viewsets.ViewSet):
    def list(self, request, *args, **kwargs):
        latest_vacancies = Vacancy.objects.order_by("-created_at")[:5]

        if latest_vacancies:
            serializer = VacancyListSerializer(latest_vacancies, many=True)
            return Response(serializer.data)
        else:
            return Response(
                {"error": "No vacancies found"}, status=status.HTTP_404_NOT_FOUND
            )
