from abc import ABC
from maps.constant.coordinate_cell import CoordinateCell
from maps.constant.dofus_map import DofusMap
from typing import TypeVar, Generic

T = TypeVar('T')


class MapCell(ABC, Generic[T]):
    def get_id(self) -> int:
        """
        Return the cell id.

        :return: the cell id. Start at 0
        """
        pass

    def walkable(self) -> bool:
        """
        Check if the cell is walkable.

        :return: True if walkable, False otherwise
        """
        pass

    def map(self) -> DofusMap['MapCell']:
        """
        Get the container map

        :return: the parent DofusMap
        """
        pass

    def coordinate(self) -> CoordinateCell['MapCell']:
        """
        Get the coordinate of the current cell
        This is equivalent to {@code new CoordinateCell<>(cell)}

        Note: this method will always recreate a new {@link CoordinateCell} instance

        :return: The cell coordinate
        """
        pass
