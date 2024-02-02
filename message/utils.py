from django.core.mail import get_connection, EmailMessage
from main import settings


def send_emails(recipient_email: str, message_url: str):
    with get_connection(
        host=settings.EMAIL_HOST,
        port=settings.EMAIL_PORT,
        username=settings.EMAIL_HOST_USER,
        password=settings.EMAIL_HOST_PASSWORD,
        use_tls=settings.EMAIL_USE_TLS,
    ) as connection:
        subject = "TEST BACKEND"
        email_from = settings.EMAIL_HOST_USER

        msg = EmailMessage(
            subject, message_url, email_from, [recipient_email], connection=connection
        )
        msg.content_subtype = "html"  # Main content is now text/html
        msg.send()

    return
