import pytest
from app import create_app
from app.db import db
from app.models.planet import Planet
from flask.signals import request_finished
from dotenv import load_dotenv
import os

load_dotenv()

@pytest.fixture
def app():
    test_config = {
        "TESTING": True,
        "SQLALCHEMY_DATABASE_URI": os.environ.get('SQLALCHEMY_TEST_DATABASE_URI')
    }
    app = create_app(test_config)

    @request_finished.connect_via(app)
    def expire_session(sender, response, **extra):
        db.session.remove()

    with app.app_context():
        db.create_all()
        yield app

    with app.app_context():
        db.drop_all()


@pytest.fixture
def client(app):
    return app.test_client()

@pytest.fixture
def two_saved_planets(app):
    planet_Mercury = Planet(name="Mercury", description="The smallest and closest planet to the Sun with a rocky surface and no moons.", diameter=4879)
    planet_Venus = Planet(name="Venus", description="A rocky planet with a thick, toxic atmosphere and surface temperatures hot enough to melt lead.", diameter=12104)

    db.session.add_all([planet_Mercury, planet_Venus])
    db.session.commit()