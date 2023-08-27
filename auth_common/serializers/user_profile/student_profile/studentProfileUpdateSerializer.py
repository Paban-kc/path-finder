from rest_framework import serializers

from auth_common.model.student import Student



class StudentProfileUpdateSerializer(serializers.ModelSerializer):

    class Meta:
        model= Student
        fields="__all__"