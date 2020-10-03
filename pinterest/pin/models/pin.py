''' Pins Model '''

import uuid
from django.db import models

# Utils Model
from pinterest.utils.models import GeneralModel


class Pin(GeneralModel):
    ''' Pin Model '''

    # Id
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)

    # Pin data
    title = models.CharField('title of the pin', null=True, blank=True, max_length=100)
    link = models.CharField('link of the pin', null=True, blank=True, max_length=100)
    # date = models.DateTimeField('date of the pin', max_length=250)
    about = models.TextField('description of the pin', max_length=500, null=True, blank=True)
    picture = models.ImageField(
        'picture',
        upload_to='users/pictures/'
    )
    # Reference to User (Belongs)
    user = models.ForeignKey(
        to="users.User",
        on_delete=models.SET_NULL,
        null=True,
    )
    board = models.ForeignKey(
        to="board.Board",
        on_delete=models.SET_NULL,
        null=True,
    )

    def __str__(self):
        return str(self.title)
