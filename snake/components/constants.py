from enum import Enum
from typing import NamedTuple


class Direction(NamedTuple):
    direction: str
    increment: tuple = ()


class Directions(Enum):

    @classmethod
    def can_set_direction(cls, old_dir, new_dir):
        cmpl_directions = {
            cls.UP: cls.DOWN,
            cls.DOWN: cls.UP,
            cls.RIGHT: cls.LEFT,
            cls.LEFT: cls.RIGHT
        }

        return new_dir != cmpl_directions[old_dir]

    @property
    def direction(self):
        return self.value.direction

    @property
    def increment(self):
        return self.value.increment

    UP = Direction("UP", (0, 1))
    DOWN = Direction("DOWN", (0, -1))
    RIGHT = Direction("RIGHT", (1, 0))
    LEFT = Direction("LEFT", (-1, 0))
