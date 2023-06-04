from __future__ import annotations

from dataclasses import dataclass

from .abstract_map_cell import AbstractMapCell
from .constant import Direction


@dataclass(frozen=True)
class CoordinateCell:
    _cell: AbstractMapCell
    x: int
    y: int

    def __init__(self, cell: AbstractMapCell):
        object.__setattr__(self, "_cell", cell)

        width: int = cell.map.dimensions.width
        line: int = cell.id // (width * 2 - 1)
        column: int = cell.id - line * (width * 2 - 1)
        offset: int = column % width

        object.__setattr__(self, "y", line - offset)
        object.__setattr__(self, "x", (cell.id - (width - 1) * self.y) // width)

    def direction_to(self, target: CoordinateCell) -> Direction:
        """Compute the direction to the target cell

        :param target: The target cell
        :type target: AbstractCoordinateCell
        :return: The Direction
        :rtype: Direction
        """
        if self.x == target.x:
            if self.y > target.y:
                return Direction.SOUTH_WEST
            else:
                return Direction.NORTH_EAST
        elif target.x > self.x:
            return Direction.SOUTH_EAST
        else:
            return Direction.NORTH_WEST

    def distance(self, target: CoordinateCell) -> int:
        """Get the cell distance
        Note: Don't compute a pythagorean distance but "square" distance.


        :param target: The target cell
        :type target: AbstractCoordinateCell
        :return: The distance, in cell numbers
        :rtype: int
        """
        return abs(self.x - target.x) + abs(self.y - target.y)
