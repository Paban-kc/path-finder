from rest_framework import serializers
from auth_common.model.application import Application
from auth_common.serializers.register_student.studentProfileCreateSerializer import StudentSerializer
from auth_common.serializers.vacancy.vacancyListSerializer import VacancyListSerializer


class ApplicationDeleteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Application
        fields = ["id"]