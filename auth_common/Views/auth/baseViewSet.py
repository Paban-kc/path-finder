from rest_framework import generics, permissions


class BaseViewSet(generics.ListCreateAPIView, generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [permissions.IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save()

    def perform_update(self, serializer):
        serializer.save()

    def get_serializer_context(self):
        context = super().get_serializer_context()
        context["user"] = self.request.user
        return context

    def get_serializer_class(self):
        if self.request.method == "GET":
            if self.lookup_field in self.kwargs:  # Check if it's a detail view
                return self.retrieve_serializer_class
            else:
                return self.list_serializer_class
        elif self.request.method == "POST":
            return self.create_serializer_class
        elif self.request.method in ["PUT", "PATCH"]:
            return self.update_serializer_class
        else:  # DELETE
            return self.destroy_serializer_class
