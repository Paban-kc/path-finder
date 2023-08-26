from rest_framework import serializers
from auth_common.model.internship import Internship


class InternshipSubmissionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Internship
        exclude = ["organization"]

    def create(self, validated_data):
        user = self.context["request"].user
        organization = user.organization_user
        validated_data["organization"] = organization
        internship = Internship.objects.create(**validated_data)
        return internship

    def to_representation(self, instance):
        data = super().to_representation(instance)
        data["organization_name"] = instance.organization.organization_name
        data["website"] = instance.organization.website
        data["contact_person"] = instance.organization.contact_person
        data["phone_no"] = instance.organization.phone_no
        data["alt_phone_no"] = instance.organization.alt_phone_no
        return data
