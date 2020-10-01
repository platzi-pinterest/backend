""" Pin App. """
from django.apps import AppConfig
from django.utils.translation import gettext_lazy as _


class PinAppConfig(AppConfig):
    """ Pin app config."""

    name = "pinterest.pin"
    verbose_name = _("pin")
