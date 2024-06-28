from rest_framework import serializers

from auth_common.model.organization import Organization
from auth_common.serializers.register_organization.organizationSerializer import (
    OrganizationSerializer,
)

from ...model import Vacancy


class VacancyListSerializer(serializers.ModelSerializer):
    organization = OrganizationSerializer()
    total_applications = serializers.SerializerMethodField()

    class Meta:
        model = Vacancy
        fields = "__all__"

    def get_total_applications(self,instance):
        return instance.applications.count()
