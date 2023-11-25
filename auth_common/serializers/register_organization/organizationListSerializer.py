from rest_framework import serializers
from rest_framework.exceptions import ValidationError
from auth_common.model.auth.user import User

from auth_common.model.organization import Organization
from auth_common.serializers.auth.userBaseSerializer import UserSerializer


class OrganizationListSerializer(serializers.ModelSerializer):
    user = serializers.PrimaryKeyRelatedField(queryset=User.objects.all())

    class Meta:
        model = Organization
        fields = "__all__"
        ref_name = "OrganizationSerializer"
