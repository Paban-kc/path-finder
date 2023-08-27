from rest_framework import serializers

from auth_common.model.feedback import Feedback

class FeedbackRetrieveSerializer(serializers.ModelSerializer):
    class Meta:
        model = Feedback
        fields = '__all__'
