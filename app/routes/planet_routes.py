from flask import Blueprint, abort, make_response, request, Response
from app.models.planet import Planet
from app.models.moon import Moon
from ..db import db
from .route_utilities import validate_model , create_model

bp = Blueprint("planet_bp", __name__, url_prefix="/planets")

@bp.post("")
def create_planet():
    request_body = request.get_json()

    new_planet = Planet.from_dict(request_body)
    
    db.session.add(new_planet)
    db.session.commit()

    return new_planet.to_dict(), 201

@bp.get("")
def get_all_planets():
    query = db.select(Planet)

    name_param = request.args.get("name")
    if name_param:
        query = query.where(Planet.name.ilike(f"%{name_param}%"))

    description_param = request.args.get("description")
    if description_param:
        query = query.where(Planet.description.ilike(f"%{description_param}%"))

    max_param = request.args.get("max")
    if max_param:
        query = query.where(Planet.diameter <= max_param)

    min_param = request.args.get("min")
    if min_param:
        query = query.where(Planet.diameter >= min_param)

    query = query.order_by(Planet.id)
    planets = db.session.scalars(query)

    return [planet.to_dict() for planet in planets]

@bp.get("<planet_id>")
def get_one_planet(planet_id):
    planet = validate_model(Planet, planet_id)

    return planet.to_dict()

@bp.put("<planet_id>")
def update_planet(planet_id):
    planet = validate_model(Planet, planet_id)

    request_body = request.get_json()
    planet.name = request_body["name"]
    planet.description = request_body["description"]
    planet.moons = request_body["moons"]
    planet.diameter = request_body["diameter"]

    db.session.commit()

    return Response(status=204, mimetype="application/json")


@bp.delete("<planet_id>")
def delete_planet(planet_id):
    planet = validate_model(Planet, planet_id)
    db.session.delete(planet)
    db.session.commit()

    return Response(status=204, mimetype="application/json")

@bp.post("/<planet_id>/moons")
def create_moon_with_planet(planet_id):
    planet = validate_model(Planet, planet_id)

    request_body = request.get_json()
    request_body["planet_id"] = planet.id
    return create_model(Moon, request_body)

@bp.get("/<planet_id>/moons")
def get_moons_by_planet(planet_id):
    planet = validate_model(Planet, planet_id)
    response = [moon.to_dict() for moon in planet.moons]
    return response

