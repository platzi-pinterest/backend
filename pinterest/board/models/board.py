''' Boards Model '''

import uuid
from django.db import models

# Utils Model
from pinterest.utils.models import GeneralModel


class Board(GeneralModel):
    ''' Board Model '''

    # Id
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)

    # Board data
    name = models.CharField('name of board', max_length=100)
    date = models.DateTimeField('date to keep the board', null=True, blank=True, max_length=250)
    secret = models.BooleanField('the board is secret?', default=False)

    # Reference to User (Belongs)

    def __str__(self):
        return str(self.name)
