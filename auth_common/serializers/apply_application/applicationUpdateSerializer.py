from rest_framework import serializers

from auth_common.model.application import Application

class ApplicationUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Application
        fields = "__all__"

    def update(self, instance, validated_data):
        instance.date_applied = validated_data.get('date_applied', instance.date_applied)
        instance.status = validated_data.get('status', instance.status)
        instance.resume = validated_data.get('resume', instance.resume)
        instance.cover_letter = validated_data.get('cover_letter', instance.cover_letter)
        instance.is_approved = validated_data.get('is_approved', instance.is_approved)
        
        instance.student_profile = validated_data.get('student_profile', instance.student_profile)
        instance.vacancy = validated_data.get('vacancy', instance.vacancy)
        
        instance.save()
        return instance
