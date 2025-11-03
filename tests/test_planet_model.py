from app.db import db
from app.models.planet import Planet

def test_from_dict():
    # Arrange
    planet_data = {
        "name": "Mercury",
        "description": "The smallest and closest planet to the Sun with a rocky surface and no moons.",
        "moons": 0,
        "diameter": 4879
        }

    # Act
    new_planet = Planet.from_dict(planet_data)


    # Assert
    assert isinstance(new_planet, Planet)
    assert new_planet.name == "Mercury"
    assert new_planet.description == "The smallest and closest planet to the Sun with a rocky surface and no moons."
    assert new_planet.moons == 0
    assert new_planet.diameter == 4879

def test_to_dict():
    # Arrange
    new_planet = Planet(id=1, name="Mercury",
        description="The smallest and closest planet to the Sun with a rocky surface and no moons.",
        moons=0,
        diameter=4879)

    # Act
    response_dict = new_planet.to_dict()

    # Assert
    assert response_dict == {
        "id":1,
        "name":"Mercury",
        "description":"The smallest and closest planet to the Sun with a rocky surface and no moons.",
        "moons": 0,
        "diameter": 4879
        }
    assert len(response_dict)==5


