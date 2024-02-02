import pytest
from client.models import Client
from mailing.utils import filter_clients_by_mailing


@pytest.mark.django_db
@pytest.mark.parametrize(
    "client_filter, expected_count",
    [
        ({"mobile_code": "123", "tag": "tag1"}, 1),
        ({"mobile_code": "123", "tag": "tag2"}, 2),
        ({"mobile_code": "789", "tag": "tag3"}, 0),
        ({"mobile_code": "456"}, 1),
        ({"tag": "tag1"}, 1),
        ({}, 0),
    ],
)
def test_filter_clients_by_mailing(client_filter, expected_count, sample_clients):
    q_params = {key: value for key, value in client_filter.items() if value is not None}
    filtered_clients = filter_clients_by_mailing(Client.objects.all(), q_params)

    assert filtered_clients.count() == expected_count
