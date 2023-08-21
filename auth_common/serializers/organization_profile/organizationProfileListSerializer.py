from rest_framework import serializers
from ...model.organization import OrganizationProfile


class OrganizationProfileListSerializer(serializers.Serializer):

    class Meta:
        model=OrganizationProfile
        fields="__all__"