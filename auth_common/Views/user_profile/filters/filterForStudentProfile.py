from django_filters import rest_framework as filters
import django_filters
from ....model.student import Organization, Student

class StudentFilter(django_filters.FilterSet):
    class Meta:
        model = Student
        fields = {
            'id': ['exact'],
            'user__first_name': ['icontains'],
            'user__last_name': ['icontains'],
        }
