from django_filters import rest_framework as filters

from ....model.student import Student


class FilterForStudent(filters.FilterSet):
    registered_date = filters.DateFromToRangeFilter()

    class Meta:
        model = Student
        fields = ["id"]
        search_fields = ["first_name", "id"]
