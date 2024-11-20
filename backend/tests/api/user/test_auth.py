import pytest


@pytest.mark.django_db
def test_authenticated_request(auth_api_client):
    response = auth_api_client.get('/api/user/auth/me/')

    assert response.status_code == 200
