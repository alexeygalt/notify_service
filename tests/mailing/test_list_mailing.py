import pytest
from django.urls import reverse

from mailing.serializers import MailingListSerializer, MailingBaseSerializer
from tests import factories


@pytest.mark.django_db
def test_list(client):
    boards = factories.MailingFactory.create_batch(5)

    response = client.get(reverse('list_all_mailing'))

    expected_response = MailingListSerializer(instance=boards, many=True).data

    assert response.status_code == 200
    assert response.data == expected_response
