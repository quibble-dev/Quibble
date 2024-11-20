import pytest
from rest_framework.test import APIClient
from rest_framework.authtoken.models import Token

from django_core.apps.user.models import Profile, User


@pytest.fixture
def user():
    """Creates and returns a user."""
    return User.objects.create(email='test@test.com', password='testpass')


@pytest.fixture
def user_profile(user):
    """Creates and returns a user profile"""
    return Profile.objects.create(user=user, username='test')


@pytest.fixture
def api_client():
    """Retuns a DRF API client."""
    return APIClient()


@pytest.fixture
def auth_api_client(api_client, user, user_profile):
    """Returns an authenticated API client."""
    token, _ = Token.objects.get_or_create(user=user)
    # authenticate user
    api_client.credentials(
        HTTP_AUTHORIZATION=f"Bearer {token.key}", HTTP_PROFILE_ID=str(user_profile.id)
    )
    return api_client
