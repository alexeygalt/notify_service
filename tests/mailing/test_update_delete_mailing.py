import pytest
from django.urls import reverse
import json


@pytest.mark.django_db
def test_delete_mailing(client, custom_mailing):
    response = client.delete(reverse("update_delete_mailing", args=[custom_mailing.pk]))

    assert response.status_code == 204


@pytest.mark.django_db
@pytest.mark.parametrize(
    "update_data, expected_status_code",
    [
        (
            {
                "start_datetime": "2023-01-01T12:00:00Z",
                "end_datetime": "2023-01-02T12:00:00Z",
                "message_text": "Updated message",
                "client_filter": {"mobile_code": 123, "tag": "updated_tag"},
                "time_interval": "08:00-17:00",
            },
            200,
        ),
        (
            {
                "start_datetime": "2023-02-01T12:00:00Z",
                "end_datetime": "2023-01-02T12:00:00Z",
                "message_text": "New message",
                "client_filter": {"mobile_code": 123, "tag": "new_tag"},
                "time_interval": "08:00-17:00",
            },
            400,
        ),
        (
            {
                "start_datetime": "2023-01-01T12:00:00Z",
                "end_datetime": "2023-01-02T12:00:00Z",
                "message_text": "Test message",
                "client_filter": {"mobile_code": 123, "tag": "tag123"},
                "time_interval": "10:00-09:00",
            },
            400,
        ),
    ],
)
def test_update_mailing(client, custom_mailing, update_data, expected_status_code):
    response = client.put(
        reverse("update_delete_mailing", args=[custom_mailing.pk]),
        data=json.dumps(update_data),
        content_type="application/json",
    )

    assert response.status_code == expected_status_code
