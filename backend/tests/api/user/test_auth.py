import pytest


@pytest.mark.django_db
def test_user_auth_request(auth_api_client, user, user_profile):
    response = auth_api_client.get('/api/user/me/')

    assert response.status_code == 200

    data = response.data
    assert data['user']['email'] == user.email
    assert data['id'] == user_profile.id
    assert data['username'] == user_profile.username


@pytest.mark.django_db
def test_user_unauth_request(api_client):
    response = api_client.get('/api/user/me/')

    assert response.status_code == 401


@pytest.mark.django_db
def test_user_login(api_client, user, token):
    payload = dict(email=user.email, password='testpass')

    response = api_client.post('/api/user/auth/login/', payload, format='json')

    assert response.status_code == 200

    data = response.data
    assert data['token'] == token.key


@pytest.mark.django_db
def test_user_logout(auth_api_client):
    response = auth_api_client.post('/api/user/auth/logout/')

    assert response.status_code == 200
