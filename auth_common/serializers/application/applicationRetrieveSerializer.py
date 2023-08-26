from rest_framework import serializers
from auth_common.model.application import Application


class ApplicationRetrieveSerializer(serializers.ModelSerializer):
    class Meta:
        model = Application
        fields = "__all__"
