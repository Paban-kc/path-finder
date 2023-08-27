from django_filters import rest_framework as filters
from auth_common.model.organization import Organization


class FilterForOrganization(filters.FilterSet):
    registered_date = filters.DateFromToRangeFilter()

    class Meta:
        model = Organization
        fields = ["id"]
        search_fields = ["organization_name", "id"]
