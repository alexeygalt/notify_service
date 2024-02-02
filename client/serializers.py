from rest_framework import serializers
from rest_framework.exceptions import ValidationError
from client.models import Client
import logging
import pytz

logger = logging.getLogger("app")


class ClientBaseSerializer(serializers.ModelSerializer):
    TIMEZONES = tuple(zip(pytz.all_timezones, pytz.all_timezones))

    timezone = serializers.ChoiceField(
        choices=TIMEZONES,
        required=False,
        help_text="example format: Europe/Berlin: ",
    )

    class Meta:
        model = Client
        fields = "__all__"

    def check_phone(self, phone: str):
        if Client.objects.filter(phone_number=phone).exists():
            raise ValidationError("Клиент с данным номером уже существует")

    def is_valid(self, raise_exception=False):
        valid = super().is_valid(raise_exception=False)
        if not valid:
            logger.error(f"Validation errors: {self.errors}")
            return super().is_valid(raise_exception=True)

        return super().is_valid(raise_exception=True)


class ClientCreateSerializer(ClientBaseSerializer):
    def create(self, validated_data: dict):
        super().check_phone(validated_data.get("phone_number"))
        instance = super().create(validated_data)
        logger.info(f"Object {instance} created successfully")
        return instance

    class Meta:
        model = Client
        fields = "__all__"


class ClientUpdateSerializer(ClientBaseSerializer):
    def update(self, instance: Client, validated_data: dict):
        if instance.phone_number != validated_data.get("phone_number"):
            super().check_phone(validated_data.get("phone_number"))
        instance = super().update(instance, validated_data)
        logger.info(f"Object {instance} updated successfully")
        return instance
