# Generated by Django 5.0.1 on 2024-02-01 11:08

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("client", "0004_alter_client_timezone"),
        ("mailing", "0005_mailing_time_interval"),
        ("message", "0003_alter_message_options"),
    ]

    operations = [
        migrations.AlterField(
            model_name="message",
            name="client_id",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                related_name="messages",
                to="client.client",
            ),
        ),
        migrations.AlterField(
            model_name="message",
            name="mailing_id",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                related_name="messages",
                to="mailing.mailing",
            ),
        ),
    ]
