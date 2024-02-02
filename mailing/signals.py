from django.db.models.signals import post_save
from django.dispatch import receiver
from client.models import Client
from mailing.models import Mailing
from mailing.tasks import sending_mail
from mailing.utils import filter_clients_by_mailing, is_within_time_interval
from message.models import Message
import logging

logger = logging.getLogger('app')


@receiver(post_save, sender=Mailing)
def create_messages_objects_by_mailing(sender, instance: Mailing, created, **kwargs):
    if created:
        if not instance.time_interval:
            clients = filter_clients_by_mailing(client_queryset=Client.objects.all(),
                                                client_filter=instance.client_filter)
        else:
            clients = filter_clients_by_mailing(client_queryset=Client.objects.all(),
                                                client_filter=instance.client_filter)

            clients = [client for client in clients if
                       is_within_time_interval(client_timezone=client.timezone, time_interval=instance.time_interval)]

        for client in clients:
            message = Message.objects.create(send_status=Message.MessageStatus.NOT_SENT, client_id=client,
                                             mailing_id=instance)
            logging.info(f"Message {message.id} created . Client {client.id}")
        sending_mail.delay()
