# Generated by Django 5.0.1 on 2024-01-26 13:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("client", "0001_initial"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="client",
            options={
                "ordering": ["id"],
                "verbose_name": "Клиент",
                "verbose_name_plural": "Клиенты",
            },
        ),
        migrations.AlterField(
            model_name="client",
            name="timezone",
            field=models.IntegerField(
                blank=True, null=True, verbose_name="Часовой пояс"
            ),
        ),
    ]
