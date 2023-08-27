from rest_framework import serializers

from auth_common.model.student import Student



class StudentProfileListSerializer(serializers.ModelSerializer):

    class Meta:
        model= Student
        fields="__all__"