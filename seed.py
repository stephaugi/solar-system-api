from app import create_app, db
from app.models.planet import Planet

my_app = create_app()
with my_app.app_context():
    planets = [
    Planet(name="Mercury", description="The smallest and closest planet to the Sun with a rocky surface and no moons.", moons=0, diameter=4879),
    Planet(name="Venus", description="A rocky planet with a thick, toxic atmosphere and surface temperatures hot enough to melt lead.", moons=0, diameter=12104),
    Planet(name="Earth", description="Our home planet, the only known world to support life, with one natural satellite, the Moon.", moons=1, diameter=12742),
    Planet(name="Mars", description="The Red Planet, known for its iron oxide surface and the largest volcano in the solar system, Olympus Mons.", moons=2, diameter=6779),
    Planet(name="Jupiter", description="The largest planet, a gas giant with a Great Red Spot and dozens of moons including Ganymede.", moons=79, diameter=139820),
    Planet(name="Saturn", description="A gas giant famous for its beautiful ring system and many moons, including Titan.", moons=83, diameter=116460),
    Planet(name="Uranus", description="An ice giant that rotates on its side, with a pale blue color due to methane in its atmosphere.", moons=27, diameter=50724),
    Planet(name="Neptune", description="The farthest known planet, an ice giant with strong winds and a deep blue appearance.", moons=14, diameter=49244)
]
    db.session.add_all(planets)
    db.session.commit()

