# Generated by Django 5.0.1 on 2024-02-01 11:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('client', '0003_alter_client_tag'),
    ]

    operations = [
        migrations.AlterField(
            model_name='client',
            name='timezone',
            field=models.CharField(blank=True, max_length=32, null=True, verbose_name='Часовой пояс'),
        ),
    ]