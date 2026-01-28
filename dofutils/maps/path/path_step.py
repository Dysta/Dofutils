from __future__ import annotations

from dataclasses import dataclass

from dofutils.maps.constant.direction import Direction
from dofutils.maps.coordinate_cell import CoordinateCell


@dataclass(frozen=True)
class PathStep:
    cell: CoordinateCell
    direction: Direction

    def __str__(self) -> str:
        return "{%s, %s}" % (self.cell.id, self.direction.name)
