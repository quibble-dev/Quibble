import pytest


@pytest.mark.django_db
class TestUsers:
    api_endpoint = '/api/v1/user/users/'

    def get_api_endpoint_with_id(self, id):
        return f'{self.api_endpoint}{id}/'

    def test_get_users(self, api_client):
        response = api_client.get(self.api_endpoint)

        assert response.status_code == 200
        data = response.data
        assert isinstance(data, list)

    def test_retrieve_user(self, auth_api_client, user):
        url = self.get_api_endpoint_with_id(user.id)

        response = auth_api_client.get(url)

        assert response.status_code == 200
        data = response.data
        assert data['email'] == user.email
