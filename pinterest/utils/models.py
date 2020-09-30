"""Django models utilities."""

# Django
from django.db import models


class GeneralModel(models.Model):
    """Event Up base model.
    GeneralModel acts as an abstract base class from which every
    other model in the project will inherit. This class provides
    every table with the following attributes:

        + status (ENUM): System status value of object
        + created (DateTime): System the datetime the object was created.
        + modified (DateTime): System the last datetime the object was modified.
        + deleted (DateTime): System the last datetime the object was deleted.
    """

    STATUS_CHOICES = (
        ('active', ('Active element')),
        ('inactive', ('Inactive element')),
    )

    status = models.CharField(
        'status',
        max_length=32,
        choices=STATUS_CHOICES,
        default='active',
        help_text='Status of the object base.'
    )

    created = models.DateTimeField(
        'created at',
        auto_now_add=True,
        help_text='Date time on which the object was created.'
    )
    modified = models.DateTimeField(
        'modified at',
        auto_now=True,
        help_text='Date time on which the object was last modified.'
    )
    deleted = models.DateTimeField(
        'deleted at',
        auto_now=True,
        help_text='Date time on which the object was delete.'
    )

    class Meta:
        """Meta option."""
        # Allow in al models/contrlores/etc...
        abstract = True
        # Config
        get_latest_by = 'created'
        ordering = ['-status', '-created', '-modified', '-deleted']
