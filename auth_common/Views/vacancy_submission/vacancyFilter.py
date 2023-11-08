from django_filters import rest_framework as django_filters

from auth_common.model.vacancy import Vacancy


class VacancyFilter(django_filters.FilterSet):
    title = django_filters.CharFilter(lookup_expr="exact")
    location = django_filters.CharFilter(lookup_expr="exact")
    industry = django_filters.CharFilter(lookup_expr="exact")
    duration = django_filters.NumberFilter()
    job_type = django_filters.CharFilter(lookup_expr="exact")
    experience_level = django_filters.CharFilter(lookup_expr="exact")
    status = django_filters.CharFilter(lookup_expr="exact")
    salary = django_filters.NumberFilter()

    class Meta:
        model = Vacancy
        fields = [
            "title",
            "location",
            "industry",
            "duration",
            "job_type",
            "experience_level",
            "status",
            "salary",
        ]
