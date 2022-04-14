import pytest


@pytest.mark.django_db
def test_add_pokemon(auth_client):
    """Add a single pokemon"""
    # Pass valid parameters
    payload = {
        "name": "Pikachu",
        "height_cm": 50,
        "weight_kg": 20,
        "type": "ELECTRIC",
        "description": "A yellow pokemon.",
    }
    response = auth_client.post("/api/pokemons", payload)
    assert response.status_code == 201


@pytest.mark.django_db
def test_add_pokemon_fail(auth_client):
    """Fail to add a single pokemon"""
    # Pass invalid height, weight and type
    payload = {
        "name": "Pikachu",
        "height_cm": -50,
        "weight_kg": -20,
        "type": "ijustmadethisup",
        "description": "A yellow pokemon.",
    }
    response = auth_client.post("/api/pokemons", payload)
    assert response.status_code == 400


@pytest.mark.django_db
def test_list_public(client):
    """Get list of all public pokemons"""
    # Validate that there are 50 pokemons
    response = client.get("/api/pokemons")
    data = response.data
    assert response.status_code == 200
    assert data["count"] == 50  # There are 50 pokemons due to data migration
    assert data["next"] is not None
    assert data["previous"] is None
    assert len(data["results"]) == 10  # Default page size


@pytest.mark.django_db
def test_list_private(auth_client):
    """Get a list of all pokemons created by a user"""
    # Add a pokemon
    payload = {
        "name": "Pikachu",
        "height_cm": 50,
        "weight_kg": 20,
        "type": "ELECTRIC",
        "description": "A yellow pokemon.",
    }
    auth_client.post("/api/pokemons", payload)

    # Validate that only 1 pokemon is sent back
    response = auth_client.get("/api/my_pokemons")
    data = response.data
    assert response.status_code == 200
    assert data["count"] == 1
    assert data["next"] is None
    assert data["previous"] is None
    assert len(data["results"]) == 1


@pytest.mark.django_db
def test_detail(auth_client):
    """Get detail of a single pokemon"""
    # In this case we will search for diglett
    response = auth_client.get("/api/pokemons/diglett")
    data = response.data

    # Validate some fields
    assert response.status_code == 200
    assert data["name"] == "diglett"
    assert data["type"] == "GROUND"


@pytest.mark.django_db
def test_detail_fail(auth_client):
    """Get detail of a single pokemon that doesn't exist"""
    # In this case we will search for agumon
    response = auth_client.get("/api/pokemons/agumon")

    # Validate that it doesn't exist
    assert response.status_code == 404


@pytest.mark.django_db
def test_update_field_fail(auth_client):
    """Update pokemon that doesn't belong to user"""
    # In this case we will update diglett
    payload = {
        "height_cm": 100,
        "weight_kg": 20,
        "type": "FLYING",
        "description": "A very powerful pokemon.",
    }
    response = auth_client.patch("/api/pokemons/diglett", payload)

    # Validate that user has no permissions to do this action
    assert response.status_code == 403


@pytest.mark.django_db
def test_update_field(auth_client):
    """Update pokemon that does belong to user"""
    # Add pikachu
    payload = {
        "name": "Pikachu",
        "height_cm": 50,
        "weight_kg": 20,
        "type": "ELECTRIC",
        "description": "A yellow pokemon.",
    }
    auth_client.post("/api/pokemons", payload)

    # Next, update fields
    payload = {
        "height_cm": 1,
        "weight_kg": 1,
        "type": "FLYING",
        "description": "A very powerful pokemon.",
    }
    response = auth_client.patch("/api/pokemons/Pikachu", payload)

    # Validate that user has permissions to do this action
    assert response.status_code == 200


@pytest.mark.django_db
def test_delete_fail(auth_client):
    """Delete pokemon that doesn't belong to user"""
    # In this case we will delete diglett
    response = auth_client.delete("/api/pokemons/diglett")

    # Validate that user has no permissions to do this action
    assert response.status_code == 403


@pytest.mark.django_db
def test_delete(auth_client):
    """Delete pokemon that does belong to user"""
    # Add Pikachu
    payload = {
        "name": "Pikachu",
        "height_cm": 50,
        "weight_kg": 20,
        "type": "ELECTRIC",
        "description": "A yellow pokemon.",
    }
    auth_client.post("/api/pokemons", payload)

    # Next, delete Pikachu
    response = auth_client.delete("/api/pokemons/Pikachu")

    # Validate that user has permissions to do this action
    assert response.status_code == 204
