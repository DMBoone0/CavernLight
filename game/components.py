"""
Author: Dillon Boone
License: MIT

Collection of ECS components.
"""

from dataclasses import dataclass

# Map data
@dataclass
class Position:
    x: int
    y: int

@dataclass
class Direction:
    x: int
    y: int

@dataclass
class Renderable:
    sprite_id: str


# Combat Data
@dataclass
class Health:
    max_hp: int
    curr_hp: int


# Categories
@dataclass
class Collidable:
    pass

@dataclass
class PlayerControlled:
    pass

@dataclass
class Encounter:
    pass