""" Category App. """
from django.apps import AppConfig
from django.utils.translation import gettext_lazy as _


class CategoryAppConfig(AppConfig):
    """ Category app config."""

    name = "pinterest.category"
    verbose_name = _("category")
