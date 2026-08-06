from __future__ import annotations

from dataclasses import dataclass

from .constant import Direction
from .dofus_map import DofusMap


@dataclass(frozen=True)
class CoordinateCell:
    id: int
    map: DofusMap
    x: int
    y: int

    walkable: bool = True
    sight_blocking: bool = False

    def __init__(
        self,
        map: DofusMap,
        id: int,
        walkable: bool = True,
        sight_blocking: bool = False,
    ):
        """
        Initialize a CoordinateCell instance.

        :param map: The map this cell belong to
        :param id: The id of the cell in the map
        :param walkable: Whether the cell is walkable, defaults to True
        :param sight_blocking: Whether the cell blocks sight, defaults to False
        :type map: AbstractMap
        :type id: int
        :type walkable: bool, optional defaults to True
        :type sight_blocking: bool, optional defaults to False
        """
        width: int = map.dimensions.width
        line: int = id // (width * 2 - 1)
        column: int = id - line * (width * 2 - 1)
        offset: int = column % width

        object.__setattr__(self, "y", line - offset)
        object.__setattr__(self, "x", (id - (width - 1) * self.y) // width)
        object.__setattr__(self, "id", id)
        object.__setattr__(self, "walkable", walkable)
        object.__setattr__(self, "sight_blocking", sight_blocking)
        object.__setattr__(self, "map", map)

    def eq(self, target: CoordinateCell) -> bool:
        """
        Check if the current coordinate cell is equal to the target

        :param target: The target coordinate cell
        :type target: CoordinateCell
        :return: True if the cells are equal, false otherwise
        :rtype: bool
        """
        return self == target

    def eq_coordinate(self, x: int, y: int) -> bool:
        """
        Check if the current coordinate cell is equal to the given coordinate

        :param x: The x coordinate
        :type x: int
        :param y: The y coordinate
        :type y: int
        :return: True if the cells are equal, false otherwise
        :rtype: bool
        """
        return self.x == x and self.y == y

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
