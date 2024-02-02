from django.contrib import admin
from mailing.models import Mailing


@admin.register(Mailing)
class MailingAdmin(admin.ModelAdmin):
    list_display = ("id", "start_datetime", "end_datetime", "time_interval")
    search_fields = (
        "id",
    )
    ordering = (
        "id",
        "start_datetime",
        "end_datetime",
    )
