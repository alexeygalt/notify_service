import pytest
from django.urls import reverse


@pytest.mark.django_db
def test_create_client(client):
    response = client.post(
        reverse("create_client"),
        data={
            "timezone": "Africa/Abidjan",
            "phone_number": "74207175758",
            "mobile_operator_code": 2147483647,
            "tag": "string",
        },
    )
    expected_response = {
        "id": response.data["id"],
        "timezone": response.data.get("timezone"),
        "phone_number": response.data.get("phone_number"),
        "mobile_operator_code": response.data.get("mobile_operator_code"),
        "tag": response.data.get("tag"),
    }

    assert response.status_code == 201
    assert response.data == expected_response


@pytest.mark.django_db
@pytest.mark.parametrize(
    "data, expected_status",
    [
        (
            {
                "timezone": "Africa/Abidjan",
                "phone_number": "74207175758",
                "mobile_operator_code": "21474a83647",
                "tag": "string",
            },
            400,
        ),
        (
            {
                "timezone": "Invalid/Timezone",
                "phone_number": "74207175758",
                "mobile_operator_code": 2147483647,
                "tag": "string",
            },
            400,
        ),
        (
            {
                "timezone": "Africa/Abidjan",
                "phone_number": "7427175758",
                "mobile_operator_code": 2147483647,
                "tag": "string",
            },
            400,
        ),
        (
            {
                "timezone": "Africa/Abidjan",
                "mobile_operator_code": 2147483647,
                "tag": "string",
            },
            400,
        ),
        (
            {
                "timezone": "Africa/Abidjan",
                "phone_number": "7427175758",
                "mobile_operator_code": 2147483647,
                "tag": "string",
            },
            400,
        ),
    ],
)
def test_create_client_invalid_data(client, data, expected_status):
    response = client.post(reverse("create_client"), data=data)
    assert response.status_code == 400
