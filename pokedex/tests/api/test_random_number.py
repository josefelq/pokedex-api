import pytest


@pytest.mark.django_db
def test_get_number(client):
    """Validate that data is sent back on endpoint"""
    response = client.get("/api/random_number")
    data = response.data

    assert "data" in data
