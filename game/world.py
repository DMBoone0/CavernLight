"""
Author: Dillon Boone
License: MIT

Class defining an ECS world.
"""

from collections import defaultdict
from typing import Type

class World:
    def __init__(self):
        self._next_entity_id = 0
        # ComponentType -> {entity id: component instance}
        self.components = defaultdict(dict)
        self.entities = set()

    # Creates and stores a new entity, returns the id of that entity.
    def create_entity(self) -> int:
        eid = self._next_entity_id
        self._next_entity_id += 1
        self.entities.add(eid)
        return eid
    
    def add_component(self, eid: int, component):
        self.components[type(component)][eid] = component
    
    def get_component(self, component):
        return self.components[type(component)]
    
    def remove_entity(self, eid):
        self.entities.discard(eid)
        for component_dict in self.components:
            component_dict.pop(eid, None)