"""
Author: Dillon Boone
License: MIT

Manages the translation between pygame events and the Command objects that will be passed around within the engine
"""
from config import *
from .command import Command

class CommandDispatcher:
    def __init__(self):
        # (event.type, event.attr) -> command
        self.bindings = {}

    # Returns event -> command mapping
    def handle_event(self, event):
        if (event.type, event.attr) in self.bindings:
            return self.bindings[(event.type, event.attr)]
        elif(event.type, ) in self.bindings:
            return self.bindings[(event.type, )]
        else:
            return None

    # command to event
    def bind_key(self, event, command):
        self.keybinds[(event.type, event.attr)] = function