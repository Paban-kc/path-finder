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
        exclude = ["student_profile", "vacancy"]

    def to_representation(self, instance):
        data = super().to_representation(instance)

        user = {
            "first_name": instance.student_profile.user.first_name,
            "last_name": instance.student_profile.user.last_name,
            "gender": instance.student_profile.user.gender,
            "email": instance.student_profile.user.email,
        }

        student_profile_data = data.pop("student_profile_data")

        vacancy_data = {
            "title": instance.vacancy.title,
            "description": instance.vacancy.description,
            "start_date": instance.vacancy.start_date,
            "end_date": instance.vacancy.end_date,
            "location": instance.vacancy.location,
            "compensation": instance.vacancy.compensation,
            "requirements": instance.vacancy.requirements,
            "application_deadline": instance.vacancy.application_deadline,
            "qualifications": instance.vacancy.qualifications,
            "benefits": instance.vacancy.benefits,
            "contact_email": instance.vacancy.contact_email,
            "contact_phone": instance.vacancy.contact_phone,
            "organization": instance.vacancy.organization.id,
        }

        final_representation = {
            "student_profile": {**user, **student_profile_data},
            "vacancy": vacancy_data,
            "application": {
                "id": data["id"],
                "created_at": data["created_at"],
                "updated_at": data["updated_at"],
                "date_applied": data["date_applied"],
                "status": data["status"],
                "resume": data["resume"],
                "cover_letter": data["cover_letter"],
            },
        }

        return final_representation
