from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework import status
from auth_common.model.placement import Placement
from auth_common.serializers.placement.placementListSerializer import (
    PlacementListSerializer,
)


class PublicPlacementListView(viewsets.ReadOnlyModelViewSet):
    queryset = Placement.objects.all()
    serializer_class = PlacementListSerializer

    def list(self, request, *args, **kwargs):
        queryset = self.filter_queryset(self.get_queryset())
        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
