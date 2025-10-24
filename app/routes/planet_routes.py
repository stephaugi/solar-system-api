from flask import Blueprint, abort, make_response, request
from app.models.planet import Planet
from ..db import db

planets_bp = Blueprint("planet_bp", __name__, url_prefix="/planets")

@planets_bp.post("")
def create_planet():
    request_body = request.get_json()
    name_from_request_body = request_body["name"]
    description_from_request_body = request_body["description"]
    moons_from_request_body = request_body["moons"]
    diameter_from_request_body = request_body["diameter"]

    new_planet = Planet(
        name=name_from_request_body, 
        description=description_from_request_body,
        moons=moons_from_request_body,
        diameter=diameter_from_request_body)
    
    db.session.add(new_planet)
    db.session.commit()

    response = {
        "id": new_planet.id,
        "name": new_planet.name,
        "description": new_planet.description,
        "moons": new_planet.moons,
        "diameter": new_planet.diameter
    }

    return response, 201

@planets_bp.get("")
def get_all_planets():
    query = db.select(Planet).order_by(Planet.id)
    planets = db.session.scalars(query)
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

    query = db.select(Planet).where(Planet.id == planet_id)
    planet = db.session.scalar(query)
    if not planet:
        response = {"message": f"planet {planet_id} not found"}
        abort(make_response(response, 404))
    return planet
