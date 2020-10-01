''' Categories Model '''

from django.db import models

# Utils Model
from pinterest.utils.models import GeneralModel


class Category(GeneralModel):
    ''' Category Model '''

    # Category data
    name = models.CharField('name of category', max_length=100)

    def __str__(self):
        return str(self.name)
