from __future__ import annotations

from abc import ABC
from dataclasses import dataclass
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from .abstract_map import AbstractMap
    from .coordinate_cell import CoordinateCell


@dataclass(frozen=True)
class AbstractMapCell(ABC):
    id: int
    walkable: bool
    map: AbstractMap
    coordinate: CoordinateCell
