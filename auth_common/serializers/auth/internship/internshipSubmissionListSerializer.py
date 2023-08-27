from rest_framework import serializers

from ....model import Internship

class InternshipSubmissionListSerializer(serializers.ModelSerializer):

    class Meta:
        model=Internship
        fields="__all__"