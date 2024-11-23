from django_filters import rest_framework as django_filters

from auth_common.model.vacancy import Vacancy


class VacancyFilter(django_filters.FilterSet):
    location = django_filters.CharFilter(lookup_expr="exact")
    duration = django_filters.CharFilter(lookup_expr="exact")
    job_type = django_filters.CharFilter(lookup_expr="exact")
    salary = django_filters.NumberFilter(lookup_expr="gte")
    application_deadline = django_filters.DateFilter(lookup_expr="lte")

    class Meta:
        model = Vacancy
        fields = [
            "location",
            "duration",
            "job_type",
            "salary",
            "application_deadline",
        ]