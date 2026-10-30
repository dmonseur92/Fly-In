from pydantic import BaseModel, Field, field_validator, ValidationError
from enum import Enum


class ZoneType(Enum):
    NORMAL = "normal"
    BLOCKED = "blocked"
    RESTRICTED = "restricted"
    PRIORITY = "priority"

class Zone(BaseModel):
    name: str
    x: int
    y: int
    color: str | None = None
    max_drones: int | None = Field(default=1, gt=0)
    type: ZoneType = ZoneType.NORMAL
    start: bool = Field(default=False)
    end: bool = Field(default=False)

# class StartZone(Zone):
#     max_capacity: int | None = None
#     @field_validator("max_capacity", mode="before")
#     @classmethod
#     def ignore_capacity(cls, value: object) -> None:
#         return None

# class EndZone(Zone):
#     max_capacity: int | None = None
#     @field_validator("max_capacity", mode="before")
#     @classmethod
#     def ignore_capacity(cls, value: object) -> None:
#         return None

class Connexion(BaseModel):
    zones: list[Zone]


class Map(BaseModel):
    nbr_drones: int = Field(ge=0, default=0)
    # zone_nbr: int = Field(ge=0)
    zone_list: list[Zone] = Field(default_factory=list)
    connexion_list: list[str] = Field(default_factory=list)
