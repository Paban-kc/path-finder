from rest_framework import serializers

from auth_common.model.feedback import Feedback
from auth_common.serializers.user_profile.organization_profile.organizationProfileListSerializer import OrganizationProfileListSerializer
from auth_common.serializers.user_profile.student_profile.studentProfileListSerializer import StudentProfileListSerializer

class FeedbackCreateSerializer(serializers.ModelSerializer):
    student=StudentProfileListSerializer(source="student_profile", read_only=True)
    organization=OrganizationProfileListSerializer(source="organization_profile",read_only=True)
    class Meta:
        model = Feedback
        fields = '__all__'
