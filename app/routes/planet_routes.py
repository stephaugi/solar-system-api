# As a client, I want to send a request...

# 1. ...to get all existing `planets`, so that I can see a list of `planets`, with their `id`, `name`, `description`, and other data of the `planet`.

from flask import Blueprint, abort, make_response
from app.models.planet import planets

planets_bp = Blueprint("planet_bp", __name__, url_prefix="/planets")

@planets_bp.get("")
def get_all_planets():
    planets_response = []
    for planet in planets:
        planets_response.append(
            {
                "id" : planet.id,
                "name" : planet.name,
                "description" : planet.description,
                "moons" : planet.moons,
                "diameter" : planet.diameter
            }
        )
    return planets_response

@planets_bp.get("/<planet_id>")
def get_one_planet(planet_id):
    planet = validate_planet(planet_id)

    return {
                "id" : planet.id,
                "name" : planet.name,
                "description" : planet.description,
                "moons" : planet.moons,
                "diameter" : planet.diameter
            }

def validate_planet(planet_id):
    try:
        planet_id = int(planet_id)
    except:
        response = {"message": f"planet {planet_id} invalid"}
        abort(make_response(response, 400))

    for planet in planets:
        if planet.id == planet_id:
            return planet

    response = {"message": f"planet {planet_id} not found"}
    abort(make_response(response, 404))