"""
Author: Dillon Boone
License: MIT

Map loading utility functions. Works from JSON files, but will eventually have some other formats too.
"""

import json
from pathlib import Path
from os.path import join
from .map_data import MapData

def load_map_json(filename) -> MapData:
    """Load a MapData object from a JSON file"""
    path = Path(join('data', 'maps', filename))
    with path.open("r", encoding="utf-8") as file:
        data = json.load(file)

    if 'tiles' not in data:
        raise ValueError(f'Invalid map file {path}: missing "tiles"')
    
    return MapData(
        tiles=data['tiles'],
        spawns=data.get('spawns', {}),
        entities=data.get('entities',[]),
        triggers=data.get('triggers', [])
    )