from django.db import models
from django_prometheus.models import ExportModelOperationsMixin
from django.utils import timezone
from rest_framework.exceptions import ValidationError


class Mailing(ExportModelOperationsMixin("mailing"), models.Model):
    start_datetime = models.DateTimeField(verbose_name="Дата и время запуска рассылки")
    end_datetime = models.DateTimeField(verbose_name="Дата и время окончания рассылки")
    message_text = models.TextField(verbose_name="Текст сообщения")
    client_filter = models.JSONField(verbose_name="Фильтр свойств клиентов")
    time_interval = models.CharField(
        max_length=11, null=True, blank=True, verbose_name="Временной интервал"
    )

    @property
    def is_active(self):
        return self.start_datetime <= timezone.now() <= self.end_datetime

    def __str__(self):
        return f"Рассылка {self.id}"

    class Meta:
        verbose_name = "Рассылка"
        verbose_name_plural = "Рассылки"
