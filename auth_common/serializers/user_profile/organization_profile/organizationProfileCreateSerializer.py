from rest_framework import serializers
from rest_framework.exceptions import ValidationError

from auth_common.model.organization import Organization


class OrganizationProfileCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Organization
        exclude = ["user"]

    def create(self, validated_data):
        user = self.context["request"].user

        # Check if an organization profile already exists for the user
        existing_organization = Organization.objects.filter(user=user).first()
        if existing_organization:
            raise ValidationError("Organization profile already exists for this user.")

        organization = Organization.objects.create(user=user, **validated_data)
        return organization

    def to_representation(self, instance):
        data = super().to_representation(instance)
        data["first_name"] = instance.user.first_name
        data["last_name"] = instance.user.last_name
        data["email"] = instance.user.email
        data["gender"] = instance.user.gender
        return data
