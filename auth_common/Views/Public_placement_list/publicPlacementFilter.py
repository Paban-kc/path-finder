import django_filters
from auth_common.model.placement import Placement


class PlacementStatusFilter(django_filters.FilterSet):
    class Meta:
        model = Placement
        fields = ["status"]
