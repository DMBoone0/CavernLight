"""
Author: Dillon Boone
License: MIT

Abstract base class. Scenes define the larger context for an ECS world to exist in. Scenes contain the logic for processing commands
"""

from abc import ABC, abstractmethod

class Scene(ABC):
    def __init__(self):
        self.world = None
        self.resources = {}

    @abstractmethod
    def on_enter(self, prev_scene):
        pass

    @abstractmethod
    def on_exit(self, next_scene):
        pass

    @abstractmethod
    def handle_command(self, command):
        pass

    @abstractmethod
    def render(self, renderer):
        pass

    @abstractmethod
    def update(self, dt):
        pass