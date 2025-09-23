"""
Author: Dillon Boone
License: MIT

Manages the translation between pygame events and the Command objects that will be passed around within the engine
"""
import pygame
from .command import Command, CommandType

class CommandDispatcher:
    def __init__(self):
        # (event.type, event.attr) -> command
        self.bindings = {}

    # Map a particular key to an event
    def bind_key(self, key, command_type: CommandType, payload=None):
        self.bindings[(pygame.KEYDOWN, key)] = (command_type, payload)

    # Returns event -> command mapping
    def dispatch(self, event: pygame.event.Event):
        # Handle keyboard input
        if event.type == pygame.KEYDOWN:
            key = event.key
            if (pygame.KEYDOWN, key) in self.bindings:
                cmd_type, payload = self.bindings[(pygame.KEYDOWN, key)]
                return Command(cmd_type, payload)
        
        if event.type == pygame.MOUSEBUTTONDOWN:
            return Command(CommandType.MOUSE_CLICK, payload={'button': event.button, 'pos': event.pos})