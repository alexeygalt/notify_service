from django.db.models import Q
from datetime import datetime
import pytz
from django.utils import timezone


def filter_clients_by_mailing(client_queryset, client_filter: dict):
    mobile_code = client_filter.get("mobile_code")
    tag = client_filter.get("tag")

    if mobile_code and tag:
        return client_queryset.filter(Q(mobile_operator_code=mobile_code) | Q(tag=tag))
    elif mobile_code:
        return client_queryset.filter(mobile_operator_code=mobile_code)
    elif tag:
        return client_queryset.filter(tag=tag)
    else:
        return client_queryset.none()


def is_within_time_interval(client_timezone: str, time_interval: str):
    if client_timezone is None:
        return True
    current_time_utc = timezone.now()

    # получаем текущее время клиента
    client_time_utc = current_time_utc.astimezone(pytz.timezone(client_timezone))

    # парсим time_interval

    interval_start_str, interval_end_str = time_interval.split("-")

    interval_start = datetime.strptime(interval_start_str, "%H:%M").time()
    interval_end = datetime.strptime(interval_end_str, "%H:%M").time()

    # формируем окончательный интервал
    interval_start = datetime.combine(current_time_utc, interval_start).astimezone(
        pytz.UTC
    )
    interval_end = datetime.combine(current_time_utc, interval_end).astimezone(pytz.UTC)

    return interval_start <= client_time_utc <= interval_end
