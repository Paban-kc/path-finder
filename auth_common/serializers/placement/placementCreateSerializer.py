from rest_framework import serializers
from auth_common.model.application import Application
from auth_common.model.organization import Organization
from auth_common.model.placement import Placement
from django.core.mail import send_mail
from django.conf import settings

class PlacementCreateSerializer(serializers.Serializer):
    application_id = serializers.IntegerField()
    start_date = serializers.DateField()
    end_date = serializers.DateField()
    supervisor = serializers.CharField(max_length=255)
    status = serializers.ChoiceField(choices=Placement.STATUS_CHOICES, default="ongoing")
    organization_id = serializers.IntegerField()

    def create(self, validated_data):
        application_id = validated_data["application_id"]
        organization_id = validated_data["organization_id"]

        try:
            application = Application.objects.get(pk=application_id)
            organization = Organization.objects.get(pk=organization_id)
        except Application.DoesNotExist:
            raise serializers.ValidationError("Application not found")
        except Organization.DoesNotExist:
            raise serializers.ValidationError("Organization not found")

        placement = Placement.objects.create(
            start_date=validated_data["start_date"],
            end_date=validated_data["end_date"],
            supervisor=validated_data["supervisor"],
            status=validated_data["status"],
            student=application.student_profile,
            vacancy=application.vacancy,
            organization=organization,
        )

        return placement

