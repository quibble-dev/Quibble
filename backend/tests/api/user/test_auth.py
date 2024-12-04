import pytest


@pytest.mark.django_db
class TestAuth:
    def test_authenticated_request(self, auth_api_client, user, user_profile):
        response = auth_api_client.get('/api/users/me/')

        assert response.status_code == 200
        data = response.data
        assert data['user']['email'] == user.email
        assert data['id'] == user_profile.id
        assert data['username'] == user_profile.username

    def test_unauthenticated_request(self, api_client):
        response = api_client.get('/api/users/me/')

        assert response.status_code == 401

    def test_login(self, api_client, user, token):
        payload = dict(email=user.email, password='testpass')

        response = api_client.post('/api/users/auth/login/', payload, format='json')

        assert response.status_code == 200
        data = response.data
        assert data['token'] == token.key

    def test_logout(self, auth_api_client):
        response = auth_api_client.post('/api/users/auth/logout/')

        assert response.status_code == 200

    def test_register(self, api_client):
        payload = dict(email='another@test.com', password='test')

        response = api_client.post('/api/users/auth/register/', payload, format='json')

        assert response.status_code == 201
        data = response.data
        assert data['email'] == payload['email']
