from sqlalchemy.orm import Mapped, mapped_column , relationship
from ..db import db
from typing import Optional 
from sqlalchemy import ForeignKey


class Moon(db.Model):
    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    size: Mapped[int]
    description: Mapped[str]
    planet_id: Mapped[Optional[int]] = mapped_column(ForeignKey("planet.id"))
    planet: Mapped[Optional["Planet"]] = relationship(back_populates="moons")

    def to_dict(self):
        response_dict = {
            "id": self.id,
            "size": self.size,
            "description": self.description
        }
        if self.planet:
            response_dict["planet"] = self.planet.to_dict()
        return response_dict
    
    @classmethod
    def from_dict(cls, dict):
        planet_id = dict.get("planet_id")
        new_moon = cls(
            size=dict["size"],
            description=dict["description"],
            planet_id=planet_id
        )
        return new_moon