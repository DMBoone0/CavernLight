"""
Author: Dillon Boone
License: MIT

Movement system for moving entities within the dungeon grid.
"""

from ..world import World
from ..components import Position, Collidable

class MovementSystem:
    def __init__(self, world: World) -> None:
        self.world = world

    def move(self, eid, dx, dy):
        positions = self.world.get_component(Position)
        collidables = self.world.get_component(Collidable)

        new_x = positions[eid].x + dx
        new_y = positions[eid].y + dy

        for entity, _ in collidables:
            if positions[entity] and positions[entity].x == new_x and positions[entity].y == new_y:
                return # collided
            
        positions[eid].x = new_x
        positions[eid].y = new_y