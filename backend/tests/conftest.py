import pytest
from rest_framework.test import APIClient
from rest_framework.authtoken.models import Token

from apps.user.models import User


@pytest.fixture
def user():
    """Creates a user."""
    return User.objects.create(email='test@test.com', password='testpass')

@pytest.fixture
def profile():
    """Creates a user profile"""
    pass


@pytest.fixture
def api_client():
    """Retuns a DRF API client."""
    return APIClient()


@pytest.fixture
def auth_api_client(api_client, user):
    """Returns an authenticated API client."""
    token, _ = Token.objects.get_or_create(user=user)
    # authenticate user
    api_client.credentials(HTTP_AUTHORIZATION=f"Token {token.key}")
    return api_client
