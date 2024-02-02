from rest_framework import serializers
from rest_framework.exceptions import ValidationError

from mailing.models import Mailing
from message.models import Message
import logging
import datetime

logger = logging.getLogger("app")


class ClientFilterSerializer(serializers.Serializer):
    mobile_code = serializers.IntegerField(required=False)
    tag = serializers.CharField(max_length=32, required=False)


class MailingBaseSerializer(serializers.ModelSerializer):
    client_filter = ClientFilterSerializer(
        help_text="Client filter JSON object with possible keys: operator_code, tag",
        required=True,
    )
    time_interval = serializers.CharField(
        max_length=11,
        help_text="Формат временного интервала: HH:mm-HH:mm",
        required=False,
    )
    CLIENT_FILTER_CHOICES = ("mobile_code", "tag")

    def validate(self, data):
        start_datetime = data["start_datetime"]
        end_datetime = data["end_datetime"]

        if start_datetime >= end_datetime:
            raise serializers.ValidationError(
                "Дата и время начала рассылки должны быть раньше даты и времени окончания рассылки"
            )

        return data

    def is_valid(self, raise_exception=False):

        valid = super().is_valid(raise_exception=False)
        if not valid:
            logger.error(f"Validation errors: {self.errors}")
            return super().is_valid(raise_exception=True)

        return super().is_valid(raise_exception=True)

    def validate_time_interval(self, value):

        try:
            start_str, end_str = value.split("-")
            start_time = datetime.datetime.strptime(start_str, "%H:%M").time()
            end_time = datetime.datetime.strptime(end_str, "%H:%M").time()
        except ValueError:
            raise ValidationError("Invalid time interval format")

        if start_time >= end_time:
            raise ValidationError("Start time must be before end time")

        return value

    class Meta:
        model = Mailing
        fields = "__all__"


class CreateMailingSerializer(MailingBaseSerializer):
    def create(self, validated_data):
        instance = super().create(validated_data)
        logger.info(f"Object {instance} created successfully")
        return instance

    class Meta:
        model = Mailing
        fields = "__all__"


class UpdateMailingSerializer(MailingBaseSerializer):
    def update(self, instance, validated_data):
        instance = super().update(instance, validated_data)
        logger.info(f"Object {instance} updated successfully")
        return instance

    class Meta:
        model = Mailing
        fields = "__all__"


class MailingListSerializer(MailingBaseSerializer):
    set_messages = serializers.SerializerMethodField(read_only=True)
    not_sent_messages = serializers.SerializerMethodField(read_only=True)

    def get_set_messages(self, obj: Mailing):
        return Message.objects.filter(
            mailing_id=obj, send_status=Message.MessageStatus.SENT
        ).count()

    def get_not_sent_messages(self, obj: Mailing):
        return Message.objects.filter(
            mailing_id=obj, send_status=Message.MessageStatus.NOT_SENT
        ).count()

    class Meta:
        model = Mailing
        fields = "__all__"
