from django.apps import AppConfig
from django.utils.translation import gettext_lazy as _


class ApisConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "blueprint_app.apis"
    verbose_name = _("APIs")
