"""
Author: Dillon Boone
License: MIT

Scene that contains the dungeon world.
"""

from scenes import Scene
from world import World
from components import Position, Direction, Collidable, PlayerControlled
from systems import MovementSystem

class DungeonScene(Scene):
    def on_enter(self, prev_scene=None):
        self.world = World()
        self.movement_system = MovementSystem(self.world)

        # spawn walls?
        # map loading probably.

        # spawn player
        player_id = self.world.create_entity()
        self.world.add_component(player_id, Position(0,0))
        self.world.add_component(player_id, Direction(1,0))
        self.world.add_component(player_id, PlayerControlled())

    def on_exit(self, next_scene):
        pass
    
    def handle_command(self, command):
        pass
    
    def render(self, renderer):
        pass

    def update(self, dt):
        pass