from rest_framework import serializers
from auth_common.model.application import Application
from auth_common.serializers.user_profile.student_profile.studentProfileListSerializer import (
    StudentProfileListSerializer,
)


class ApplicationApplyCreateSerializer(serializers.ModelSerializer):
    student_profile_data = StudentProfileListSerializer(
        source="student_profile", read_only=True
    )

    class Meta:
        model = Application
        exclude = ["student_profile", "internship"]

    def to_representation(self, instance):
        data = super().to_representation(instance)

        user = {
            "first_name": instance.student_profile.user.first_name,
            "last_name": instance.student_profile.user.last_name,
            "gender": instance.student_profile.user.gender,
            "email": instance.student_profile.user.email,
        }

        student_profile_data = data.pop("student_profile_data")

        internship_data = {
            "title": instance.internship.title,
            "description": instance.internship.description,
            "start_date": instance.internship.start_date,
            "end_date": instance.internship.end_date,
            "location": instance.internship.location,
            "compensation": instance.internship.compensation,
            "requirements": instance.internship.requirements,
            "application_deadline": instance.internship.application_deadline,
            "qualifications": instance.internship.qualifications,
            "benefits": instance.internship.benefits,
            "contact_email": instance.internship.contact_email,
            "contact_phone": instance.internship.contact_phone,
            "organization": instance.internship.organization.id,
        }

        application_data = {
            "id": data["id"],
            "created_at": data["created_at"],
            "updated_at": data["updated_at"],
            "date_applied": data["date_applied"],
            "status": data["status"],
            "resume": data["resume"],
            "cover_letter": data["cover_letter"],
        }

        final_representation = {
            "application": application_data,
            "student_profile": {**user, **student_profile_data},
            "internship": internship_data,
        }

        return final_representation
