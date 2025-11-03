from sqlalchemy.orm import Mapped, mapped_column
from ..db import db

class Planet(db.Model):
    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    name: Mapped[str]
    description: Mapped[str]
    moons: Mapped[int]
    diameter: Mapped[int]

    def to_dict(self):
        response_dict = {
            "id": self.id,
            "name": self.name,
            "description": self.description,
            "moons": self.moons,
            "diameter": self.diameter
        }
        
        return response_dict
    
    @classmethod
    def from_dict(cls, planet_data):
        return cls(name=planet_data["name"],
                description=planet_data["description"],
                moons=planet_data["moons"],
                diameter=planet_data["diameter"])

