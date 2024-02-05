import pytest
import requests
from unittest.mock import patch
from mailing.tasks import get_request


@pytest.fixture
def mock_env(monkeypatch):
    monkeypatch.setenv("PROBE_SERVER_TOKEN", "fake_token")


def test_get_request_success(mock_env):
    with patch("requests.post") as mock_post:
        mock_post.return_value.status_code = 200

        id = 1
        phone = "123456789"
        text = "Test message"

        result = get_request(id, phone, text)

        mock_post.assert_called_once_with(
            f"https://probe.fbrq.cloud/v1/send/{id}",
            headers={"Authorization": "Bearer fake_token"},
            json={"id": id, "phone": phone, "text": text},
            timeout=10,
        )

        assert result == 200


def test_get_request_failure(mock_env):
    with patch("requests.post") as mock_post:
        mock_post.side_effect = requests.exceptions.RequestException("Fake error")

        id = 1
        phone = "123456789"
        text = "Test message"

        result = get_request(id, phone, text)

        mock_post.assert_called_once_with(
            f"https://probe.fbrq.cloud/v1/send/{id}",
            headers={"Authorization": "Bearer fake_token"},
            json={"id": id, "phone": phone, "text": text},
            timeout=10,
        )
        assert result is None


def test_get_request_network_error(mock_env):
    with patch("requests.post") as mock_post:
        mock_post.side_effect = requests.exceptions.RequestException("Network error")
        mock_post.return_value.content = b"Network error content"

        id = 1
        phone = "123456789"
        text = "Test message"

        result = get_request(id, phone, text)

        mock_post.assert_called_once_with(
            f"https://probe.fbrq.cloud/v1/send/{id}",
            headers={"Authorization": "Bearer fake_token"},
            json={"id": id, "phone": phone, "text": text},
            timeout=10,
        )
        assert result is None
