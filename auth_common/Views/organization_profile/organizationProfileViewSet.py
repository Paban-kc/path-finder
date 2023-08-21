from rest_framework import viewsets
from rest_framework.filters import OrderingFilter, SearchFilter
from django_filters import rest_framework as filters
from ...model.organization import OrganizationProfile  # Adjust the import path accordingly
from ...serializers.organization_profile import (
    OrganizationProfileCreateSerializer,
    OrganizationProfileListSerializer,
    OrganizationProfileRetrieveSerializer,
    organizationProfileUpdateSerializer,
)
from rest_framework.response import Response

class OrganizationProfileViewSet(viewsets.ModelViewSet):
    filter_backends = [filters.DjangoFilterBackend, OrderingFilter, SearchFilter]
    serializer_class = OrganizationProfileCreateSerializer
    queryset = OrganizationProfile.objects.all()

    def get_serializer_class(self):
        if self.action == "list":
            return OrganizationProfileListSerializer
        elif self.action == "retrieve":
            return OrganizationProfileRetrieveSerializer
        elif self.action in ("update", "partial_update"):
            return organizationProfileUpdateSerializer
        return OrganizationProfileCreateSerializer

    def perform_create(self, serializer):
        serializer.save()

    def perform_update(self, serializer):
        serializer.save()

    def perform_destroy(self, instance):
        instance.delete()
