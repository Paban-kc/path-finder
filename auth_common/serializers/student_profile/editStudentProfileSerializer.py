from rest_framework import serializers
from ...model import StudentProfile



class StudentProfileEditSerializer(serializers.ModelSerializer):
    class Meta:
        model = StudentProfile
        # Exclude the user field, as it's not editable
        exclude = ["user"]
