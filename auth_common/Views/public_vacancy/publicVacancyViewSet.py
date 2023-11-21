from rest_framework import status
from rest_framework import viewsets
from rest_framework.permissions import AllowAny
from django.core.mail import send_mail
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters
from auth_common.Views.public_vacancy.filterForPublicVacancy import VacancyFilter
from auth_common.model.vacancy import Vacancy
from auth_common.serializers.vacancy.vacancyListSerializer import VacancyListSerializer


class PublicVacancyView(viewsets.ReadOnlyModelViewSet):
    queryset = Vacancy.objects.all()
    serializer_class = VacancyListSerializer
    permission_classes = [AllowAny]
    authentication_classes = []
    filter_backends = [DjangoFilterBackend, filters.SearchFilter]
    filterset_class = VacancyFilter
    search_fields = "__all__"
