import pytest
import json
from django.urls import reverse


@pytest.mark.django_db
def test_delete_client(client, custom_client):
    response = client.delete(reverse('update_delete_client', args=[custom_client.pk]))

    assert response.status_code == 204


@pytest.mark.django_db
@pytest.mark.parametrize("update_data, expected_status_code", [
    ({"timezone": "Africa/Abidjan", "phone_number": "79207175758", "mobile_operator_code": 2147483647, "tag": "string"},
     200),
    ({"timezone": "Europe/Berlin", "phone_number": "123456789", "mobile_operator_code": 12345, "tag": "new_tag"}, 400),
    (
            {"timezone": "Invalid/Timezone", "phone_number": "987654321", "mobile_operator_code": 54321,
             "tag": "tag123"}, 400),
    ({"timezone": "Europe/Berlin", "phone_number": "7976543210", "mobile_operator_code": 54321, "tag": "tag123"}, 400),

])
def test_update_client(client, custom_client, update_data, expected_status_code):
    response = client.put(reverse('update_delete_client', args=[custom_client.pk]),
                          data=json.dumps(update_data),
                          content_type='application/json')

    assert response.status_code == expected_status_code
