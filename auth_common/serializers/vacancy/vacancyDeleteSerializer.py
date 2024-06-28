from rest_framework import serializers

from ...model import Vacancy

class VacancyDeleteSerializer(serializers.Serializer):
    vacancy_id = serializers.IntegerField()