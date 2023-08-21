from rest_framework import serializers
from ...model.organization import OrganizationProfile 

class OrganizationProfileCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = OrganizationProfile
        exclude = ["user"]

    def create(self, validated_data):
        # Get the logged-in user
        user = self.context["request"].user

        # Try to get an existing organization profile for the user
        organization_profile, created = OrganizationProfile.objects.get_or_create(user=user, defaults=validated_data)

        # Update the organization profile data if it was not created
        if not created:
            for attr, value in validated_data.items():
                setattr(organization_profile, attr, value)
            organization_profile.save()

        return organization_profile
