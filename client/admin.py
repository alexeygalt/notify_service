from django.contrib import admin
from client.models import Client

admin.site.empty_value_display = "null"


@admin.register(Client)
class ClientAdmin(admin.ModelAdmin):
    list_display = ("id", "phone_number", "mobile_operator_code", "tag", "timezone")
    search_fields = (
        "id",
        "phone_number",
        "mobile_operator_code",
        "tag",
        "timezone",
    )
    ordering = (
        "id",
        "phone_number",
        "mobile_operator_code",
        "tag",
        "timezone",
    )
