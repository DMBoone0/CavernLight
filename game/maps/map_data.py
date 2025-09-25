"""
Author: Dillon Boone
License: MIT

Wrapper class for map data.
"""

class MapData:
    def __init__(self, tiles, spawns=None, encounters=None, triggers=None) -> None:
        self.tiles = tiles
        self.spawns = spawns or {} # { "floor_1": (x,y), "town": (x,y), ... }
        self.entities = encounters or [] # [ { name: 'slime_1', pos: (x,y), enemies: [SLIME, SLIME, ...], ... }, ... ]
        self.triggers = triggers or [] # [ { name: 'tuto_1', pos: (x,y), type: TextEvent, ... }, ... ]