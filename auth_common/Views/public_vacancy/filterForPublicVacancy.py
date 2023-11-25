from django_filters import rest_framework as filters
from auth_common.model.vacancy import Vacancy


class VacancyFilter(filters.FilterSet):
    class Meta:
        model = Vacancy
        fields = {
            "salary": ["exact"],
            "duration": ["exact"],
            "description": ["exact"],
            "start_date": ["exact"],
            "location": ["exact"],
            "requirements": ["exact"],
            "application_deadline": ["exact"],
            "contact_email": ["exact"],
            "contact_phone": ["exact"],
            "organization": ["exact"],
            "job_type": ["exact"],
        }
