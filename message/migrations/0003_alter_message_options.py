# Generated by Django 5.0.1 on 2024-01-26 13:04

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("message", "0002_alter_message_client_id_alter_message_mailing_id"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="message",
            options={
                "ordering": ["creation_datetime"],
                "verbose_name": "Сообщение",
                "verbose_name_plural": "Сообщения",
            },
        ),
    ]
