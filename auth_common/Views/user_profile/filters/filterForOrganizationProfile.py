from django_filters import rest_framework as filters
from ....model.student import Student
from auth_common.model.organization import Organization
import django_filters


class OrganizationFilter(django_filters.FilterSet):
    class Meta:
        model = Organization
        fields = {
            "id": ["exact"],
            "organization_name": ["icontains"],
        }
