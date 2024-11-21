import pytest


@pytest.mark.django_db
class TestAuthEndpoints:
    def test_authenticated_request(self, auth_api_client, user, user_profile):
        response = auth_api_client.get('/api/user/me/')

        assert response.status_code == 200

        data = response.data
        assert data['user']['email'] == user.email
        assert data['id'] == user_profile.id
        assert data['username'] == user_profile.username

    def test_unauthenticated_request(self, api_client):
        response = api_client.get('/api/user/me/')

        assert response.status_code == 401

    def test_login(self, api_client, user, token):
        payload = {"email": user.email, "password": "testpass"}

        response = api_client.post('/api/user/auth/login/', payload, format='json')

        assert response.status_code == 200

        data = response.data
        assert data['token'] == token.key

    def test_logout(self, auth_api_client):
        response = auth_api_client.post('/api/user/auth/logout/')

        assert response.status_code == 200