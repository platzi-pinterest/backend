""" Pins Serializer """

# Django REST Framework
from rest_framework import serializers

# Models
from pinterest.pin.models import Pin


class PinModelSerializer(serializers.ModelSerializer):
    """ Pin model serializer """

    id = serializers.CharField(source='pk', read_only=True)

    class Meta:
        """Meta class."""

        # fields = '__all__'
        model = Pin
        # read_only_fields
        fields = (
            'id',
            'picture',
            'title',
            'about',
            'link',
            'user',
            'board'
        )


class CreateUpdatePinSerializer(PinModelSerializer):
    """Create pin serializer."""

    def create(self, data):
        # Get uiser context
        user = self.context['request'].user
        return Pin.objects.create(**data, user=user)
