""" Categories Serializer """

# Django REST Framework
from rest_framework import serializers

# Models
from pinterest.category.models import Category


class CategoryModelSerializer(serializers.ModelSerializer):
    """ Category model serializer """

    id = serializers.IntegerField(source='pk', read_only=True)

    class Meta:
        """Meta class."""

        # fields = '__all__'
        model = Category
        # read_only_fields
        fields = (
            'id',
            'name',
        )
