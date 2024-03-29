# Generated by Django 5.0.1 on 2024-01-26 12:38

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Client",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "phone_number",
                    models.CharField(
                        max_length=11,
                        unique=True,
                        validators=[
                            django.core.validators.RegexValidator(
                                message="Введенный номер не соответствует формату 7 XXX XXX XX XX",
                                regex="^7[0-9]{10}$",
                            )
                        ],
                    ),
                ),
                (
                    "mobile_operator_code",
                    models.IntegerField(verbose_name="Код мобильного оператора"),
                ),
                ("tag", models.CharField(max_length=255, verbose_name="Тег")),
                ("timezone", models.IntegerField(verbose_name="Часовой пояс")),
            ],
        ),
    ]
