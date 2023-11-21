from django_filters import rest_framework as filters
from auth_common.model.vacancy import Vacancy


class VacancyFilter(filters.FilterSet):
    class Meta:
        model = Vacancy
        fields = {
            "title": ["exact"],
            "industry": ["exact"],
            "salary": ["exact"],
            "duration": ["exact"],
            "description": ["exact"],
            "start_date": ["exact"],
            "end_date": ["exact"],
            "location": ["exact"],
            "compensation": ["exact"],
            "requirements": ["exact"],
            "application_deadline": ["exact"],
            "responsibilities": ["exact"],
            "qualifications": ["exact"],
            "benefits": ["exact"],
            "contact_email": ["exact"],
            "contact_phone": ["exact"],
            "is_featured": ["exact"],
            "organization": ["exact"],
            "job_type": ["exact"],
            "experience_level": ["exact"],
        }
