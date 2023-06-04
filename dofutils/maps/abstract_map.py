from __future__ import annotations

from abc import ABC, abstractmethod
from dataclasses import dataclass

from ..value import Dimension
from .abstract_map_cell import AbstractMapCell


@dataclass(frozen=True)
class AbstractMap(ABC):
    """Base dofus map type"""

    size: int
    dimensions: Dimension

    @abstractmethod
    def get_cell(self, id: int) -> AbstractMapCell:
        """Return a cell by its id

        :param id: The cell Id
        :type id: int
        :raises NotImplementedError: Raised if called from abstract class
        :return: The cell
        :rtype: AbstractMapCell
        """
        raise NotImplementedError
