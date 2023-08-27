from rest_framework import serializers

from auth_common.model.organization import Organization


class OrganizationProfileListSerializer(serializers.ModelSerializer):
    class Meta:
        model= Organization
        fields="__all__"