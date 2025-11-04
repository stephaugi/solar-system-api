from ..db import db
from flask import abort, make_response

def validate_model(cls, id):
    try:
        id = int(id)
    except:
        response = {"message": f"{cls.__name__} {id} invalid"}
        abort(make_response(response, 400))

    query = db.select(cls).where(cls.id == id)
    model = db.session.scalar(query)
    if not model:
        response = {"message": f"{cls.__name__} {id} not found"}
        abort(make_response(response, 404))
    return model

def create_model(cls, model_data):
    try:
        new_model = cls.from_dict(model_data)
        
    except KeyError as error:
        response = {"details": "Invalid data"}
        abort(make_response(response, 400))
    
    db.session.add(new_model)
    db.session.commit()

    return new_model.to_dict(), 201