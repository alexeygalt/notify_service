import pytest
from mailing.utils import is_within_time_interval
from freezegun import freeze_time


@pytest.mark.parametrize(
    "client_timezone, time_interval, expected_result",
    [
        ("Europe/Moscow", "09:00-17:00", True),
        ("Europe/Moscow", "22:00-23:00", False),
        (None, "09:00-17:00", True),
    ],
)
@freeze_time("2023-01-01 12:00:00")
def test_is_within_time_interval(client_timezone, time_interval, expected_result):
    assert is_within_time_interval(client_timezone, time_interval) == expected_result
