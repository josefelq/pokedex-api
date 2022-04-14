import pytest
from django.contrib.auth import get_user_model
from rest_framework.test import APIClient
from rest_framework_simplejwt.tokens import RefreshToken


CustomUser = get_user_model()


@pytest.fixture
def user():
    user = CustomUser.objects.create_user(
        email="brock@kanto.com", password="Professor123!"
    )
    return user


@pytest.fixture
def client():
    return APIClient()


@pytest.fixture
def auth_client(user):
    client = APIClient()
    refresh = RefreshToken.for_user(user)
    client.credentials(HTTP_AUTHORIZATION=f"Bearer {refresh.access_token}")
    return client
