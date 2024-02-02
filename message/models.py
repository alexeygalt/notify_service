from django.db import models
from django.utils import timezone
from django_prometheus.models import ExportModelOperationsMixin
from client.models import Client
from mailing.models import Mailing


class Message(ExportModelOperationsMixin("message"), models.Model):
    class MessageStatus(models.TextChoices):
        SENT = "sent", "Отправлено"
        NOT_SENT = "not_sent", "Не отправлено"

    creation_datetime = models.DateTimeField(default=timezone.now)
    send_status = models.CharField(max_length=32, choices=MessageStatus.choices)
    mailing_id = models.ForeignKey(
        Mailing, on_delete=models.CASCADE, related_name="messages"
    )
    client_id = models.ForeignKey(
        Client, on_delete=models.CASCADE, related_name="messages"
    )

    def __str__(self):
        return f"Сообщение {self.id}"

    class Meta:
        verbose_name = "Сообщение"
        verbose_name_plural = "Сообщения"
        ordering = ["creation_datetime"]
