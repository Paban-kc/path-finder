from rest_framework import mixins, viewsets

from .mixins import ListMixin, RetrieveMixin


class IntGenericViewSet(viewsets.GenericViewSet):
    resource_name = None

    list_serializer_class = None
    retrieve_serializer_class = None
    create_serializer_class = None
    update_serializer_class = None

    def get_serializer_class(self):
        cls = getattr(self, self.action + "_serializer_class", None)
        if cls:
            return cls
        return super().get_serializer_class()


class IntViewSetBase(
    ListMixin,
    RetrieveMixin,
    mixins.CreateModelMixin,
    mixins.UpdateModelMixin,
    mixins.DestroyModelMixin,
    IntGenericViewSet,
):
    pass


class IntReadOnlyViewSetBase(
    ListMixin,
    RetrieveMixin,
    IntGenericViewSet,
):
    pass
