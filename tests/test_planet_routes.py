from app.db import db
from app.models.planet import Planet

def test_get_all_planets_with_no_records(client):
    # Act
    response = client.get("/planets/")
    response_body = response.get_json()

    # Assert
    assert response.status_code == 200
    assert response_body == []

def test_get_one_book(client, two_saved_planets):
    # Act
    response = client.get("/planets/1")
    response_body = response.get_json()

    # Assert
    assert response.status_code == 200
    assert response_body == {
        "id": 1,
        "name": "Mercury",
        "description": "The smallest and closest planet to the Sun with a rocky surface and no moons.",
        "moons": 0,
        "diameter": 4879
    }

def test_create_one_planet(client):
    # Act
    response = client.post("/planets/", json={
        "name": "Mercury",
        "description": "The smallest and closest planet to the Sun with a rocky surface and no moons.",
        "moons": 0,
        "diameter": 4879
    })
    response_body = response.get_json()

    # Assert
    assert response.status_code == 201
    assert response_body == {
        "id": 1,
        "name": "Mercury",
        "description": "The smallest and closest planet to the Sun with a rocky surface and no moons.",
        "moons": 0,
        "diameter": 4879
    }

def test_update_one_planet(client, two_saved_planets):
    # Act
    response = client.put("/planets/1", json={
        "name": "UpdatedMercury",
        "description": "Updated The smallest and closest planet to the Sun with a rocky surface and no moons.",
        "moons": 1,
        "diameter": 48799
    })

    # Assert
    assert response.status_code == 204
    query = db.select(Planet).where(Planet.id == 1)
    query_result = db.session.execute(query).scalar_one()
    assert query_result.name == "UpdatedMercury"
    assert query_result.description == "Updated The smallest and closest planet to the Sun with a rocky surface and no moons."
    assert query_result.moons == 1
    assert query_result.diameter == 48799