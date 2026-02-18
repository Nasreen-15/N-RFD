from django.apps import AppConfig


class OpportunitiesConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "apps.opportunities"   # ✅ must match INSTALLED_APPS
