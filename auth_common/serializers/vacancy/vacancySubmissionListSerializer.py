from rest_framework import serializers

from ...model import Vacancy

class VacancySubmissionListSerializer(serializers.ModelSerializer):

    class Meta:
        model=Vacancy
        fields="__all__"