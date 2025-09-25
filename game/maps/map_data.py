"""
Author: Dillon Boone
License: MIT

Wrapper class for map data. Stores map layer data and walkability.
"""

from dataclasses import dataclass, field
from typing import List, Dict, Tuple

@dataclass
class MapData:
    tiles: List[List[int]]  # 2D grid, 0 is floor, 1 for wall
    spawns: Dict[str, Tuple[int, int]] = field(default_factory=dict) # { "name": (x, y) }
    entities: List[Dict] = field(default_factory=list)  # { "type": str, "pos": (x, y) }
    triggers: List[Dict] = field(default_factory=list)  # future expansion

    def is_walkable(self, x: int, y: int) -> bool:
        """Check if a tile can be walked on."""
        try:
            return self.tiles[y][x] == 0
        except IndexError:
            return False