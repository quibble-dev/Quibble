import pytest
from rest_framework.authtoken.models import Token
from rest_framework.test import APIClient, urlencode

from django_core.apps.user.models import Profile, User


@pytest.fixture
def user():
    """Creates and returns a user."""
    return User.objects.create_user(email='test@test.com', password='testpass')


@pytest.fixture
def token(user):
    """Creats and returns an auth token."""
    return Token.objects.create(user=user)


@pytest.fixture
def user_profile(user):
    """Creates and returns a user profile"""
    return Profile.objects.create(user=user, username='test')


@pytest.fixture
def api_client():
    """Retuns a DRF API client."""
    return APIClient()


@pytest.fixture
def auth_api_client(api_client, user_profile, token):
    """Returns an authenticated API client."""
    api_client.credentials(
        HTTP_AUTHORIZATION=f"Bearer {token.key}", HTTP_PROFILE_ID=str(user_profile.id)
    )
    return api_client
