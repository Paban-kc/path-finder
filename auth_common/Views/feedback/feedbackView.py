from rest_framework import viewsets

from auth_common.model.feedback import Feedback
from auth_common.serializers.feedback.feedbackCreateSerializer import (
    FeedbackCreateSerializer,
)
from ...serializers.feedback import (
    FeedbackCreateSerializer,
    FeedbackListSerializer,
    FeedbackRetrieveSerializer,
    FeedbackUpdateSerializer,
)


class FeedbackViewSet(viewsets.ModelViewSet):
    queryset = Feedback.objects.all()
    serializer_class = FeedbackCreateSerializer

    def get_serializer_class(self):
        if self.action == "create":
            return FeedbackCreateSerializer
        elif self.action == "list":
            return FeedbackListSerializer
        elif self.action == "retrieve":
            return FeedbackRetrieveSerializer
        elif self.action == "partial_update":
            return FeedbackUpdateSerializer
        else:
            return super().get_serializer_class()
