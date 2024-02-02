import os
from celery import Celery
from celery.schedules import crontab
from main.settings import env

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "main.settings")
app = Celery("main")
app.config_from_object("django.conf:settings", namespace="CELERY")
app.autodiscover_tasks()

app.conf.beat_schedule = {
    "api_call_and_send": {
        "task": "mailing.tasks.sending_mail",
        "schedule": crontab(
            minute="*/1",
        ),
    },
    "send_stats_to_email": {
        "task": "message.tasks.get_and_sent_stats",
        "schedule": crontab(minute=0, hour=0),
        "args": (env.str("RECIPIENT_EMAIL"),),
    },
}
