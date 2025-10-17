# 1. Define a `Planet` class with the attributes `id`, `name`, and `description`, and one additional attribute
# 1. Create a list of `Planet` instances

class Planet:
    def __init__(self, id, name, description, moons, diameter):
        self.id = id
        self.name = name
        self.description = description
        self.moons = moons
        self.diameter = diameter

planets = [
    Planet(1, "Mercury", "The smallest and closest planet to the Sun with a rocky surface and no moons.", 0, 4879),
    Planet(2, "Venus", "A rocky planet with a thick, toxic atmosphere and surface temperatures hot enough to melt lead.", 0, 12104),
    Planet(3, "Earth", "Our home planet, the only known world to support life, with one natural satellite, the Moon.", 1, 12742),
    Planet(4, "Mars", "The Red Planet, known for its iron oxide surface and the largest volcano in the solar system, Olympus Mons.", 2, 6779),
    Planet(5, "Jupiter", "The largest planet, a gas giant with a Great Red Spot and dozens of moons including Ganymede.", 95, 139820),
    Planet(6, "Saturn", "A gas giant famous for its beautiful ring system and many moons, including Titan.", 83, 116460),
    Planet(7, "Uranus", "An ice giant that rotates on its side, with a pale blue color due to methane in its atmosphere.", 27, 50724),
    Planet(8, "Neptune", "The farthest known planet, an ice giant with strong winds and a deep blue appearance.", 14, 49244)
]