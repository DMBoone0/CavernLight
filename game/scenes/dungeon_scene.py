"""
Author: Dillon Boone
License: MIT

Scene that contains the dungeon world.
"""

from .scene import Scene
from world import World
from component import Position, Collidable, PlayerControlled
from systems import MovementSystem

class DungeonScene(Scene):
    def on_enter(self, prev_scene=None):
        self.world = World()