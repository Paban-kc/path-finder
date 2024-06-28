from rest_framework import serializers
from auth_common.model.vacancy import Vacancy


class VacancyPostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Vacancy
        fields="__all__"

    