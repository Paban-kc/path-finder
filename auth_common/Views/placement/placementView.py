from rest_framework.response import Response
from rest_framework import status
from rest_framework import viewsets
from auth_common.model.organization import Organization
from auth_common.model.placement import Placement
from auth_common.serializers.placement.placementCreateSerializer import (
    PlacementFromApplicationSerializer,
)
from django.core.mail import send_mail
from django.conf import settings
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters
from ...serializers.placement import (
    PlacementListSerializer,
    PlacementRetrieveSerializer,
    PlacementUpdateSerializer,
    PlacementFromApplicationSerializer,
)
from rest_framework.permissions import IsAuthenticated


class PlacementFromApplicationView(viewsets.ModelViewSet):
    queryset = Placement.objects.all()
    serializer_class = PlacementFromApplicationSerializer
    filter_backends = [DjangoFilterBackend, filters.SearchFilter]
    filterset_fields = ["status"]
    search_fields = ["supervisor"]

    permission_classes = [IsAuthenticated]

    def create(self, request):
        mutable_data = request.data.copy()

        user_id = request.user.id

        try:
            organization = Organization.objects.get(user_id=user_id)
        except Organization.DoesNotExist:
            return Response(
                {"error": "Organization not found for the given user_id."},
                status=status.HTTP_404_NOT_FOUND,
            )

        mutable_data["organization_id"] = organization.id

        serializer = self.serializer_class(data=mutable_data)
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
        queryset = self.filter_queryset(self.get_queryset())
        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)

    def update(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = self.get_serializer(instance, data=request.data, partial=True)
        serializer.is_valid(raise_exception=True)
        updated_instance = serializer.save()

        new_status = serializer.validated_data.get("status")
        if new_status == "completed":
            recipient_email = updated_instance.student.user.email
            subject = "Placement Completed"
            message = "Congratulations! Your placement has been completed."
            from_email = settings.DEFAULT_FROM_EMAIL
            send_mail(subject, message, from_email, [recipient_email])

        return Response(serializer.data, status=status.HTTP_200_OK)

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
