"""Mixins General."""

# Django REST Framework
from rest_framework import status

# Utils / Response
from pinterest.utils.responses import CustomActions

# Make Actions
custom_actions = CustomActions()


class CustomCreateModelMixin:
    """
    Create a model instance.
    """

    def create(self, request, *args, **kwargs):
        """Handle HTTP POST request."""
        serializer = self.get_serializer(data=request.data)

        # Validate Model
        if not serializer.is_valid():
            data = self.custom_actions.set_response(status.HTTP_400_BAD_REQUEST,
                                                    'Error to make the object', serializer.errors)
        else:
            # Save Object
            self.perform_create(serializer)
            # Return User
            content = serializer.data
            data = self.custom_actions.set_response(status.HTTP_201_CREATED, 'Object create Success!', content)

        return self.custom_actions.custom_response(data)

    def perform_create(self, serializer):
        serializer.save()


class CustomRetrieveModelMixin:
    """
    Retrieve a model instance.
    """

    def retrieve(self, request, *args, **kwargs):
        data = None
        try:
            instance = self.get_object()
        except Exception:
            data = custom_actions.set_response(status.HTTP_400_BAD_REQUEST, 'Not found data')

        if not data:
            # Get Object
            content = self.get_serializer(instance).data
            # Return Data
            data = custom_actions.set_response(status.HTTP_200_OK, 'Get information!', content)
        # Get Status
        return custom_actions.custom_response(data)


class CustomListModelMixin:
    """
    List a queryset.
    """

    def list(self, request, *args, **kwargs):
        content = None
        queryset = self.filter_queryset(self.get_queryset())
        page = self.paginate_queryset(queryset)
        if page is not None:
            serializer = self.get_serializer(page, many=True)
            response = self.get_paginated_response(serializer.data)
            content = response.data
        else:
            serializer = self.get_serializer(queryset, many=True)
            content = serializer.data

        if content:
            data = custom_actions.set_response(status.HTTP_200_OK, 'Get information!', content)
        else:
            data = custom_actions.set_response(status.HTTP_400_BAD_REQUEST, 'Not found data')
        # Get Status
        return custom_actions.custom_response(data)


class CustomUpdateModelMixin:
    """
    Update a model instance.
    """

    def update(self, request, *args, **kwargs):
        data = None
        partial = kwargs.pop('partial', False)
        # Check if exist
        try:
            instance = self.get_object()
        except Exception:
            data = custom_actions.set_response(status.HTTP_400_BAD_REQUEST, 'Not found data')

        if not data:
            serializer = self.get_serializer(instance, data=request.data, partial=partial)
            # Validate Model
            if not serializer.is_valid():
                data = self.custom_actions.set_response(status.HTTP_400_BAD_REQUEST,
                                                        'Error to make the object', serializer.errors)
            else:
                # Save Object
                self.perform_update(serializer)
                # Attr
                if getattr(instance, '_prefetched_objects_cache', None):
                    # If 'prefetch_related' has been applied to a queryset, we need to
                    # forcibly invalidate the prefetch cache on the instance.
                    instance._prefetched_objects_cache = {}
                # Return User
                content = serializer.data
                # Return Data
                data = custom_actions.set_response(status.HTTP_200_OK, 'Get information!', content)
        # Get Status
        return custom_actions.custom_response(data)

    def perform_update(self, serializer):
        serializer.save()

    def partial_update(self, request, *args, **kwargs):
        kwargs['partial'] = True
        return self.update(request, *args, **kwargs)


class CustomDestroyModelMixin:
    """
    Destroy a model instance.
    """

    def destroy(self, request, *args, **kwargs):
        data = None
        try:
            instance = self.get_object()
        except Exception:
            data = custom_actions.set_response(status.HTTP_400_BAD_REQUEST, 'Not found data')

        if not data:
            # Delete Object
            self.perform_destroy(instance)
            # Get Status
            data = custom_actions.set_response(status.HTTP_204_NO_CONTENT, 'Object Deleted!')
        # Get Status
        return custom_actions.custom_response(data)

    def perform_destroy(self, instance):
        instance.delete()