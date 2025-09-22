"""
Author: Dillon Boone
License: MIT

Glue code that stores commands that are assigned to inputs. When input is recieved the input is delegated to the associated command.
"""
from config import *

class InputHandler:
    def __init__(self):
        self.keybinds = {}

    # Execute commands for the set of keys passed in
    def handle_input(self, keys):
        for key in self.keybinds.keys():
            if keys[key]:
                self.keybinds[key]()

    # Bind key to function
    def bind_key(self, key, function):
        self.keybinds[key] = function