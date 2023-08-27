
from rest_framework import serializers

from auth_common.model.placement import Placement

class PlacementRetrieveSerializer(serializers.ModelSerializer):
    class Meta:
        model = Placement
        fields = "__all__"
