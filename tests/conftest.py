import pytest
from tests import factories
from client.models import Client


@pytest.fixture
def sample_clients():
    return [
        Client.objects.create(
            phone_number="79123456789",
            mobile_operator_code="123",
            tag="tag1",
            timezone="Europe/Moscow",
        ),
        Client.objects.create(
            phone_number="79234567890",
            mobile_operator_code="456",
            tag="tag2",
            timezone="America/New_York",
        ),
    ]


@pytest.fixture
def custom_client():
    client = factories.ClientFactory.create()
    return client


@pytest.fixture
def custom_mailing():
    mailing = factories.MailingFactory.create()
    return mailing
