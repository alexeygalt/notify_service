# Generated by Django 5.0.1 on 2024-02-01 11:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mailing', '0004_remove_mailing_client_filter_operator_code_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='mailing',
            name='time_interval',
            field=models.CharField(blank=True, max_length=11, null=True),
        ),
    ]
