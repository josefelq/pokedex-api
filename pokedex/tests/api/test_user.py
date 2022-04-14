import pytest


@pytest.mark.django_db
def test_register_user(client):
    payload = {
        "email": "user@gmail.com",
        "password": "APassword12!",
    }

    # Register user
    response = client.post("/api/register", payload)
    data = response.data

    assert response.status_code == 201
    assert data["email"] == payload["email"]
    assert "password" not in data


@pytest.mark.django_db
def test_register_user_fail(client):
    payload = {
        "email": "incorrectemail.com",
        "password": "abc",
    }

    # Register user
    response = client.post("/api/register", payload)
    data = response.data

    assert response.status_code == 400
    assert "email" in data
    assert "password" in data


@pytest.mark.django_db
def test_login_user(client, user):
    payload = {
        "email": "brock@kanto.com",  # test@gmail.com already exists in data migration
        "password": "Professor123!",
    }
    # Login
    response = client.post("/api/login", payload)
    data = response.data

    assert response.status_code == 200
    assert "access" in data
    assert "refresh" in data


@pytest.mark.django_db
def test_login_user_fail(client, user):
    payload = {
        "email": "misty@kanto.com",  # test@gmail.com already exists in data migration
        "password": "PokemonTrainer123!",
    }
    # Login
    response = client.post("/api/login", payload)
    data = response.data

    assert response.status_code == 401
    assert "access" not in data
    assert "refresh" not in data
