from rest_framework import serializers
from auth_common.model.application import Application
from auth_common.model.organization import Organization
from auth_common.model.placement import Placement
from django.core.mail import send_mail
from notifications.models import Notification
from django.conf import settings


from rest_framework import serializers
from notifications.models import Notification
from django.core.mail import send_mail
from django.conf import settings


class PlacementFromApplicationSerializer(serializers.Serializer):
    application_id = serializers.IntegerField()
    start_date = serializers.DateField()
    end_date = serializers.DateField()
    supervisor = serializers.CharField(max_length=255)
    status = serializers.ChoiceField(
        choices=Placement.STATUS_CHOICES, default="ongoing"
    )
    organization_id = serializers.IntegerField()

    def create(self, validated_data):
        application_id = validated_data.pop("application_id")
        organization_id = validated_data.pop("organization_id")

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
            internship=application.internship,
            organization=organization,
        )

        if placement.status == "completed":
            self._send_completion_notification(placement)

        return placement

    def update(self, instance, validated_data):
        new_status = validated_data.get("status", instance.status)
        instance.status = new_status
        instance.save()

        if new_status == "completed":
            self._send_completion_notification(instance)

        return instance

    def _send_completion_notification(self, placement):
        if placement.status == "completed":
            subject = "Placement Completed"
            message = "Congratulations! Your placement has been completed."
            recipient_email = placement.student.user.email
            send_mail(subject, message, settings.DEFAULT_FROM_EMAIL, [recipient_email])

        Notification.objects.create(
            recipient=placement.student.user,
            verb="Placement marked as completed",
            description="Your placement has been marked as completed.",
        )
