from rest_framework import status
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from auth_common.Views.vacancy_post.vacancyFilter.vacancyFilter import VacancyFilter
from auth_common.model.vacancy import Vacancy
from auth_common.serializers.vacancy.vacancyRetrieveSerializer import (
    VacancyRetrieveSerializer,
)
from auth_common.serializers.vacancy.vacancyDeleteSerializer import (
    VacancyDeleteSerializer,
)
from auth_common.serializers.vacancy.vacancyListSerializer import VacancyListSerializer
from auth_common.serializers.vacancy.vacancyPostSerializer import VacancyPostSerializer
from auth_common.serializers.vacancy.vacancyUpdateSerializer import (
    VacancyUpdateSerializer,
)
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from auth_common.model.vacancy import Vacancy
from rest_framework.response import Response
from rest_framework import status


class VacancyPostView(viewsets.ModelViewSet):
    queryset = Vacancy.objects.all()
    serializer_class = VacancyPostSerializer
    permission_classes = [IsAuthenticated]
    filter_backends = (DjangoFilterBackend,)
    filterset_class = VacancyFilter

    def get_serializer_class(self):
        if self.action == "list":
            return VacancyListSerializer
        elif self.action == "retrieve":
            return VacancyRetrieveSerializer
        elif self.action == "create":
            return VacancyPostSerializer
        elif self.action in ["update", "partial_update"]:
            return VacancyUpdateSerializer
        elif self.action == "destroy":
            return VacancyDeleteSerializer

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response(
            serializer.data, status=status.HTTP_201_CREATED, headers=headers
        )
