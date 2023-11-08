from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from auth_common.model.vacancy import Vacancy
from auth_common.serializers.vacancy.vacancySubmissionCreateSerializer import VacancySubmissionSerializer
from .vacancyFilter import VacancyFilter
from rest_framework.response import Response
from rest_framework import status


class VacancySubmissionViewSet(viewsets.ModelViewSet):
    queryset = Vacancy.objects.all()
    serializer_class = VacancySubmissionSerializer
    permission_classes = [IsAuthenticated]
    filter_backends = (DjangoFilterBackend,) 
    filterset_class = VacancyFilter

    def get_queryset(self):
        queryset = Vacancy.objects.all()
        title_query = self.request.query_params.get("title", None)
        if title_query:
            queryset = queryset.filter(title__icontains=title_query)
        return queryset

    def perform_create(self, serializer):
        organization = self.request.user.organization_user
        serializer.save(organization=organization)
        return Response(serializer.data, status=status.HTTP_201_CREATED)
