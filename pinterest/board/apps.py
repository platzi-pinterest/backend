""" Board App. """
from django.apps import AppConfig
from django.utils.translation import gettext_lazy as _


class BoardAppConfig(AppConfig):
    """ Board app config."""

    name = "pinterest.board"
    verbose_name = _("board")
