from mailing.models import Mailing
from django.utils import timezone
from message.models import Message
from django.template.loader import get_template
from message.utils import send_emails
from main.celery import app
from celery.utils.log import get_task_logger
from smtplib import SMTPException, SMTPAuthenticationError


logger = get_task_logger(__name__)


@app.task
def get_and_sent_stats(email):
    completed_mailings = Mailing.objects.filter(end_datetime__lt=timezone.now())

    all_messages = [mailing.messages.all().count() for mailing in completed_mailings]
    all_sent_messages = [
        mailing.messages.filter(send_status=Message.MessageStatus.SENT).count()
        for mailing in completed_mailings
    ]
    percent = round(sum(all_sent_messages) / sum(all_messages), 2)

    ctx = {
        "time": f"Текущее время {timezone.now()}",
        "all_mailings": f"Кол-во рассылок {completed_mailings.count()}",
        "all_messages": f"Кол-во сообщений {sum(all_messages)}",
        "percent": f"Конверсия {percent}",
    }

    message = get_template("base.html").render(ctx)
    try:
        send_emails(recipient_email=email, message_url=message)
        logger.info("Sending email completed")
    except SMTPAuthenticationError as e:
        logger.error(f"Ошибка аутентификации SMTP {e}")

    except SMTPException as e:
        logger.error(f"Ошибка SMTP: {e}")

    except Exception as e:
        logger.error(f"Другая ошибка: {e}")
