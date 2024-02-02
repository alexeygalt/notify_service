import json
from django.urls import reverse
import pytest
from datetime import datetime
from mailing.models import Mailing


@pytest.mark.django_db
def test_create_mailing(client):
    data = {
        "start_datetime": "2023-01-01T12:00:00Z",
        "end_datetime": "2023-01-02T12:00:00Z",
        "message_text": "Test message",
        "client_filter": {"mobile_code": 123, "tag": "example"},
        "time_interval": "08:00-17:00",
    }

    response = client.post(
        reverse("create_mailing"),
        data=json.dumps(data),
        content_type="application/json",
    )

    assert response.status_code == 201
    assert Mailing.objects.count() == 1

    expected_start_datetime = datetime.fromisoformat(data["start_datetime"])
    expected_end_datetime = datetime.fromisoformat(data["end_datetime"])

    created_mailing = Mailing.objects.first()

    assert created_mailing.start_datetime == expected_start_datetime
    assert created_mailing.end_datetime == expected_end_datetime
    assert created_mailing.message_text == data["message_text"]
    assert created_mailing.client_filter == data["client_filter"]
    assert created_mailing.time_interval == data["time_interval"]


@pytest.mark.django_db
@pytest.mark.parametrize(
    "invalid_data, expected_status",
    [
        (
            {
                "start_datetime": "2023-01-01T12:00:00Z",
                "end_datetime": "invalid_date",
                "message_text": "Test",
                "client_filter": {"code": "123", "tag": "example"},
                "time_interval": "08:00-17:00",
            },
            400,
        ),
        (
            {
                "start_datetime": "invalid_date",
                "end_datetime": "2023-01-01T14:00:00Z",
                "message_text": "Test",
                "client_filter": {"code": "123", "tag": "example"},
                "time_interval": "08:00-17:00",
            },
            400,
        ),
        (
            {
                "start_datetime": "2023-01-01T12:00:00Z",
                "end_datetime": "2023-01-01T14:00:00Z",
                "message_text": "Test",
                "client_filter": {"code": "invalid_code", "tag": "example"},
                "time_interval": "12:00-9:00",
            },
            400,
        ),
        (
            {
                "start_datetime": "2023-01-01T12:00:00Z",
                "end_datetime": "2023-01-01T14:00:00Z",
                "message_text": "Test",
                "client_filter": {"code": "123", "tag": "example"},
                "time_interval": "invalid_interval",
            },
            400,
        ),
        (
            {
                "start_datetime": "2023-02-01T12:00:00Z",
                "end_datetime": "2023-01-01T14:00:00Z",
                "message_text": "Test",
                "client_filter": {"code": "123", "tag": "example"},
                "time_interval": "invalid_interval",
            },
            400,
        ),
    ],
)
def test_create_mailing_invalid_data(client, invalid_data, expected_status):
    response = client.post(
        reverse("create_mailing"),
        data=json.dumps(invalid_data),
        content_type="application/json",
    )

    assert response.status_code == expected_status
    assert Mailing.objects.count() == 0
