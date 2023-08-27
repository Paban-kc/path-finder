from rest_framework.response import Response
from rest_framework import status
from rest_framework import viewsets
from auth_common.model.placement import Placement
from auth_common.serializers.placement.placementCreateSerializer import (
    PlacementFromApplicationSerializer,
)
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters
from ...serializers.placement import (
    PlacementListSerializer,
    PlacementRetrieveSerializer,
    PlacementUpdateSerializer,
    PlacementFromApplicationSerializer,
)


class PlacementFromApplicationView(viewsets.ModelViewSet):
    queryset = (
        Placement.objects.all()
    )
    serializer_class = PlacementFromApplicationSerializer
    filter_backends = [DjangoFilterBackend, filters.SearchFilter]
    filterset_fields = ["status"]
    search_fields = ["supervisor"]

    def create(self, request):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            placement = serializer.save()
            return Response(
                {
                    "message": "Placement created successfully.",
                    "placement_id": placement.id,
                },
                status=status.HTTP_201_CREATED,
            )
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def list(self, request, *args, **kwargs):
        queryset = self.filter_queryset(self.get_queryset())  # Apply filters
        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)

    def get_serializer_class(self):
        if self.action == "create":
            return PlacementFromApplicationSerializer
        elif self.action == "list":
            return PlacementListSerializer
        elif self.action == "retrieve":
            return PlacementRetrieveSerializer
        elif self.action == "partial_update":
            return PlacementUpdateSerializer
        else:
            return super().get_serializer_class()
