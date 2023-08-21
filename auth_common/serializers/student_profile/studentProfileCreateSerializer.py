from rest_framework import serializers
from ...model import StudentProfile


class StudentCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = StudentProfile
        exclude = ["user"]

    def create(self, validated_data):
        # Get the logged-in user
        user = self.context["request"].user

        # Try to get an existing student profile for the user
        student_profile, created = StudentProfile.objects.get_or_create(user=user, defaults=validated_data)

        # Update the student profile data if it was not created
        if not created:
            for attr, value in validated_data.items():
                setattr(student_profile, attr, value)
            student_profile.save()

        return student_profile


        return student_profile
