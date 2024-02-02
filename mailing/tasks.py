from main.celery import app
import requests
from main.settings import env
from mailing.models import Mailing
from message.models import Message
from celery.utils.log import get_task_logger

logger = get_task_logger(__name__)


@app.task(ignore_result=False)
def get_request(id: int, phone: str, text: str):
    try:
        logger.info(f"Request for message {id} started")
        r = requests.post(f'https://probe.fbrq.cloud/v1/send/{id}',
                          headers={'Authorization': 'Bearer ' + env.str("PROBE_SERVER_TOKEN")},
                          json={"id": id,
                                "phone": phone,
                                "text": text},
                          timeout=10
                          )
        logger.info(f"Response for message-{id}  {r.content} taken")
        r.raise_for_status()
        return r.status_code
    except requests.exceptions.RequestException as e:
        logger.error(f"Error with sending mail {id} : {e}")
        return None


@app.task(ignore_result=False)
def sending_mail():
    active_mailing = [mailing.id for mailing in Mailing.objects.all() if mailing.is_active]
    messages_pull = Message.objects.filter(mailing_id__in=active_mailing, send_status=Message.MessageStatus.NOT_SENT)

    for message in messages_pull:
        client_phone = message.client_id.phone_number
        message_text = message.mailing_id.message_text
        result = get_request.apply_async(
            args=[message.id, client_phone, message_text],
            link=sent_callback.s(message_id=message.id)
        )

    return f"Mailing completed"


@app.task
def sent_callback(result, message_id, **kwargs):
    if result == 200:
        message = Message.objects.get(id=message_id)
        message.send_status = Message.MessageStatus.SENT
        message.save()
        logger.info(f"Message {message_id} is sent")
