from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework import status
from rest_framework.filters import SearchFilter, OrderingFilter
from auth_common.model.internship import Internship
from auth_common.serializers.auth.internship.internshipSubmissionCreateSerializer import (
    InternshipSubmissionSerializer,
)


class InternshipSubmissionViewSet(viewsets.ModelViewSet):
    queryset = Internship.objects.all()
    serializer_class = InternshipSubmissionSerializer
    permission_classes = [IsAuthenticated]
    filter_backends = [SearchFilter, OrderingFilter]
    search_fields = ["title", "description", "location", "industry"]

    def get_queryset(self):
        queryset = Internship.objects.all()
        title_query = self.request.query_params.get("title", None)
        if title_query:
            queryset = queryset.filter(title__icontains=title_query)
        return queryset

    def perform_create(self, serializer):
        organization = self.request.user.organization_user
        serializer.save(organization=organization)
        return Response(serializer.data, status=status.HTTP_201_CREATED)
