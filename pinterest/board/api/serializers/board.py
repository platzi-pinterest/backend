""" Boards Serializer """

# Django REST Framework
from rest_framework import serializers

# Models
from pinterest.board.models import Board


class BoardModelSerializer(serializers.ModelSerializer):
    """ Board model serializer """

    id = serializers.CharField(source='pk', read_only=True)

    class Meta:
        """Meta class."""

        # fields = '__all__'
        model = Board
        # read_only_fields
        fields = (
            'id',
            'name',
            'date',
            'secret'
        )


class CreateUpdateBoardSerializer(BoardModelSerializer):
    """Create board serializer."""

    def create(self, data):
        # Get uiser context
        return Board.objects.create(**data)
