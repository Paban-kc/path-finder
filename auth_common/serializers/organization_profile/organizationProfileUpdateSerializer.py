from rest_framework import serializers
from ...model.organization import OrganizationProfile


class OrganizationProfileRetireveSerializer(serializers.Serializer):
    class Meta:
        model = OrganizationProfile
        fields = "__all__"
