from rest_framework import serializers
from auth_common.model.application import Application

class ApplicationUpdateSerializer(serializers.ModelSerializer):
    # user can update only vacancy
    class Meta:
        model = Application
        fields = ["vacancy"]
