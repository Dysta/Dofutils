from __future__ import annotations

from dataclasses import dataclass

from dofutils.maps.coordinate_cell import CoordinateCell
from dofutils.maps.dofus_map import DofusMap


@dataclass(frozen=True)
class BattleFieldSight(CoordinateCell):
    sight_blocking: bool = True

    def __init__(self, map: DofusMap, id: int, walkable: bool = False, sight_blocking: bool = False):
        """
        Initialize a BattleFieldSight instance.

        :param map: The map this cell belong to
        :param id: The id of the cell in the map
        :param walkable: Whether the cell is walkable, defaults to False
        :param sight_blocking: Whether the cell blocks sight, defaults to False
        :type map: DofusMap
        :type id: int
        :type walkable: bool, optional defaults to False
        :type sight_blocking: bool, optional defaults to False
        """
        super().__init__(map, id, walkable=walkable, sight_blocking=sight_blocking)

    def between(self, target: CoordinateCell) -> int:
        """
        Calculate the number of cells between the current cell and the target cell using Manhattan distance.

        :param target: The target coordinate cell
        :type target: CoordinateCell
        :return: The number of cells between the current cell and the target cell
        :rtype: int
        """
        return abs(self.x - target.x) + abs(self.y - target.y)
