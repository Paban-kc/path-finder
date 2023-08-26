from rest_framework import serializers


class JWTSerializer(serializers.Serializer):
    """
    Serializer for JWT authentication.
    """

    token = serializers.CharField()
