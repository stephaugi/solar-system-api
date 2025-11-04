from flask import Blueprint, request , Response
from app.models.moon import Moon
from app.models.planet import Planet
from .route_utilities import create_model, validate_model 
from ..db import db

bp = Blueprint("moons_bp", __name__, url_prefix="/moons")

@bp.post("")
def create_moon():
    request_body = request.get_json()

    new_moon = Moon.from_dict(request_body)
    
    db.session.add(new_moon)
    db.session.commit()

    return new_moon.to_dict(), 201

@bp.get("")
def get_all_moons():
    query = db.select(Moon)

    description_param = request.args.get("description")
    if description_param:
        query = query.where(Moon.description.ilike(f"%{description_param}%"))

    max_param = request.args.get("max")
    if max_param:
        query = query.where(Moon.size <= max_param)

    min_param = request.args.get("min")
    if min_param:
        query = query.where(Moon.size >= min_param)

    query = query.order_by(Moon.id)
    moons = db.session.scalars(query)

    return [moon.to_dict() for moon in moons]

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

