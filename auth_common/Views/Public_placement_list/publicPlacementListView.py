import django_filters
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework import status
from auth_common.Views.Public_placement_list.publicPlacementFilter import (
    PlacementStatusFilter,
)
from auth_common.model.placement import Placement
from auth_common.serializers.placement.placementListSerializer import (
    PlacementListSerializer,
)
from rest_framework.filters import SearchFilter, OrderingFilter
from django_filters.rest_framework import DjangoFilterBackend


class PublicPlacementListView(viewsets.ReadOnlyModelViewSet):
    queryset = Placement.objects.all()
    serializer_class = PlacementListSerializer
    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
    filterset_class = PlacementStatusFilter
    search_fields = ["status"]

    def list(self, request, *args, **kwargs):
        queryset = self.filter_queryset(self.get_queryset())
        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
