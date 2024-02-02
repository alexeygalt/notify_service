from django.core.validators import RegexValidator
from django.db import models
from django_prometheus.models import ExportModelOperationsMixin


class Client(ExportModelOperationsMixin("client"), models.Model):
    phone_number = models.CharField(
        max_length=11,
        unique=True,
        validators=[
            RegexValidator(
                regex="^7[0-9]{10}$",
                message="Введенный номер не соответствует формату 7 XXX XXX XX XX",
            )
        ],
    )
    mobile_operator_code = models.IntegerField(verbose_name="Код мобильного оператора")
    tag = models.CharField(verbose_name="Тег", max_length=32, blank=True, null=True)
    timezone = models.CharField(
        verbose_name="Часовой пояс", max_length=32, null=True, blank=True
    )

    def __str__(self):
        return f"Клиент {self.id}"

    class Meta:
        verbose_name = "Клиент"
        verbose_name_plural = "Клиенты"
        ordering = ["id"]
