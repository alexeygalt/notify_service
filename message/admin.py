from django.contrib import admin
from django.utils.safestring import mark_safe
from message.models import Message
from django.urls import reverse


@admin.register(Message)
class MessageAdmin(admin.ModelAdmin):
    list_display = ("id", "creation_datetime", "send_status", "mailing_link", "client_link")
    search_fields = (
        "id",
    )
    ordering = (
        "mailing_id",
        "send_status",
        "client_id",
        "creation_datetime"
    )
    list_filter = ("send_status",)

    def mailing_link(self, message: Message):
        url = reverse("admin:mailing_mailing_change", args=[message.mailing_id.id])
        link = '<a href="%s">%s</a>' % (url, message.mailing_id.__str__())
        return mark_safe(link)

    mailing_link.short_description = "Рассылка"

    def client_link(self, message: Message):
        url = reverse("admin:client_client_change", args=[message.client_id.id])
        link = '<a href="%s">%s</a>' % (url, message.client_id.__str__())
        return mark_safe(link)

    client_link.short_description = "Клиент"
