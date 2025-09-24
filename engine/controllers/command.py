"""
Author: Dillon Boone
License: MIT

Expanded command pattern. Reified method call that includes a command type enum.
"""

from dataclasses import dataclass
from enum import Enum, auto
from typing import Any, Optional

class CommandType(Enum):
    MOVE_FORWARD = auto()
    MOVE_BACKWARD = auto()
    TURN_LEFT = auto()
    TURN_RIGHT = auto()
    OPEN_MENU = auto()
    QUIT_GAME = auto()
    MOUSE_CLICK = auto()

@dataclass
class Command:
    type: CommandType
    payload: Optional[dict[str, Any]] = None