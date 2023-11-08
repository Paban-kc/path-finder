from rest_framework import serializers
from auth_common.model.vacancy import Vacancy


class VacancySubmissionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Vacancy
        exclude = ["organization"]
    
    def to_search_representation(self, instance):
        data = self.to_representation(instance)
        data["organization_name"] = instance.organization.organization_name
        data["title"] = instance.title

        return data

    def to_representation(self, instance):
        data = super().to_representation(instance)
        data["organization_name"] = instance.organization.organization_name
        data["website"] = instance.organization.website
        data["contact_person"] = instance.organization.contact_person
        data["phone_no"] = instance.organization.phone_no
        data["alt_phone_no"] = instance.organization.alt_phone_no
        return data
