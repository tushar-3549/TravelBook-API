import pytest
from django.urls import reverse

@pytest.mark.django_db
def test_register_login_me_flow(api_client):
    # register
    url = "/api/v1/auth/register/"
    payload = {"username":"bob","email":"bob@example.com","password":"pass1234"}
    r = api_client.post(url, payload, format="json")
    assert r.status_code in (200, 201)

    # login
    url = "/api/v1/auth/login/"
    r = api_client.post(url, {"username":"bob","password":"pass1234"}, format="json")
    assert r.status_code == 200
    access = r.data.get("access")
    assert access

    # me
    api_client.credentials(HTTP_AUTHORIZATION=f"Bearer {access}")
    r = api_client.get("/api/v1/me/")
    assert r.status_code == 200
    assert r.data["username"] == "bob"
