from __future__ import annotations

from abc import ABC, abstractmethod
from dataclasses import dataclass

from ..value import Dimension
from .coordinate_cell import CoordinateCell


@dataclass(frozen=True)
class DofusMap(ABC):
    """Base dofus map type"""

    size: int
    dimensions: Dimension

    @abstractmethod
    def get_cell(self, id: int) -> CoordinateCell:
        """Return a cell by its id

        :param id: The cell Id
        :type id: int
        :raises NotImplementedError: Raised if called from abstract class
        :return: The cell
        :rtype: AbstractMapCell
        """
        raise NotImplementedError
