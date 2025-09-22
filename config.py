"""
Author: Dillon Boone
License: MIT

For now this is going to be the home of the more system-wide constants and imports.
Will probably be broken up later to match the MVC architecture and separation of concerns.
"""

import pygame
from pygame import Vector2 as vector2
from pygame import Vector3 as vector3
from sys import exit
from os.path import join

# Window info
WINDOW_WIDTH, WINDOW_HEIGHT = 1280, 720
CAPTION = 'CavernLight Engine'

# Default keymaps
KEY_DEFAULTS = {
    'turn_left': pygame.K_a,
    'turn_right': pygame.K_d,
    'walk_forward': pygame.K_w,
    'turn_back': pygame.K_s,
}