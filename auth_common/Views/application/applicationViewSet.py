from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated

from auth_common.model.application import Application
from auth_common.serializers.apply_application.applicationDeleteSerializer import ApplicationDeleteSerializer
from auth_common.serializers.apply_application.applicationListSerializer import ApplicationListSerializer
from auth_common.serializers.apply_application.applicationRetrieveSerializer import ApplicationRetrieveSerializer
from auth_common.serializers.apply_application.applicationCreateSerializer import ApplicationCreateSerializer

class ApplicationViewSet(viewsets.ModelViewSet):
    queryset = Application.objects.all()
    permission_classes = [IsAuthenticated]

    def get_serializer_class(self):
        if self.action == 'list':
            return ApplicationListSerializer
        elif self.action == 'retrieve':
            return ApplicationRetrieveSerializer
        elif self.action == 'create':
            return ApplicationCreateSerializer
        elif self.action == 'destroy':
            return ApplicationDeleteSerializer
        return ApplicationListSerializer
