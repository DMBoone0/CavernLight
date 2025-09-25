"""
Author: Dillon Boone
License: MIT

Scene that contains the dungeon world.
"""

from .scene import Scene
from ..world import World
from ..components import Position, Direction, Collidable, PlayerControlled
from ..systems import MovementSystem
from engine.controllers import CommandType

class DungeonScene(Scene):
    def on_enter(self, prev_scene=None):
        self.world = World()
        self.movement_system = MovementSystem(self.world)

        # spawn walls?
        # map loading probably.

        # spawn player
        self.player_id = self.world.create_entity()
        self.world.add_component(self.player_id, Position(0,0))
        self.world.add_component(self.player_id, Direction(1,0))
        self.world.add_component(self.player_id, PlayerControlled())

    def on_exit(self, next_scene):
        pass
    
    def handle_command(self, command):
        if command.type == CommandType.MOVE_FORWARD:
            directions = self.world.get_component(Direction)
            player_direction = directions[self.player_id]
            self.movement_system.move(self.player_id, player_direction.x, player_direction.y)
        elif command.type == CommandType.TURN_RIGHT:
            self.movement_system.rotate(self.player_id, False)
        elif command.type == CommandType.TURN_LEFT:
            self.movement_system.rotate(self.player_id, True)
    
    def render(self, renderer):
        pass

    def update(self, dt):
        pass