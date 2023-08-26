from time import timezone

from django.conf import settings
from rest_framework import serializers
from rest_framework.fields import CreateOnlyDefault

from .fields import CurrentUserIdDefault


class IntCreateSerializerBase(serializers.ModelSerializer):
    """
    Base serializer for create.
    """

    create_user = serializers.HiddenField(
        default=CreateOnlyDefault(CurrentUserIdDefault())
    )
    update_user = serializers.HiddenField(default=CurrentUserIdDefault())

    class Meta:
        exclude = (
            "create_date",
            "update_date",
            settings.VERSION_FIELD_NAME,
        )


class IntUpdateSerializerBase(serializers.ModelSerializer):
    """
    Base serializer for update.
    """

    create_user = serializers.HiddenField(
        default=CreateOnlyDefault(CurrentUserIdDefault())
    )
    update_user = serializers.HiddenField(default=CurrentUserIdDefault())

    class Meta:
        exclude = (
            "create_date",
            "update_date",
        )
        include = (settings.VERSION_FIELD_NAME,)
