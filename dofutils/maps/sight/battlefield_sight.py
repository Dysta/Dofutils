from __future__ import annotations

from collections.abc import Callable, Iterator
from math import ceil, floor

from dofutils.maps.coordinate_cell import CoordinateCell
from dofutils.maps.dofus_map import DofusMap


class BattlefieldSight:
    def __init__(self, battlefield: DofusMap):
        self.battlefield = battlefield

    def between(self, source: CoordinateCell, target: CoordinateCell) -> bool:
        return self.from_cell(source).is_free(target)

    def from_cell(self, source: CoordinateCell) -> CellSight:
        return CellSight(self, source)

    def get_cell_by_coordinates(self, x: int, y: int) -> CoordinateCell:
        return self.battlefield.get_cell(
            x * self.battlefield.dimensions.width + y * (self.battlefield.dimensions.width - 1)
        )


class CellSight:
    def __init__(self, battlefield: BattlefieldSight, source: CoordinateCell):
        self.battlefield, self.source = battlefield, source

    def to(self, target: CoordinateCell) -> Iterator[CoordinateCell]:
        if self.source == target:
            return iter(())
        return self._same_x(target) if self.source.x == target.x else self._line(target)

    def is_free(self, target: CoordinateCell) -> bool:
        return all(not cell.sight_blocking or cell == target for cell in self.to(target))

    def accessible(self) -> list[CoordinateCell]:
        return [
            self.battlefield.battlefield.get_cell(i)
            for i in range(self.battlefield.battlefield.size)
            if self.is_free(self.battlefield.battlefield.get_cell(i))
        ]

    def blocked(self) -> list[CoordinateCell]:
        return [
            self.battlefield.battlefield.get_cell(i)
            for i in range(self.battlefield.battlefield.size)
            if not self.is_free(self.battlefield.battlefield.get_cell(i))
        ]

    def for_each(self, consumer: Callable[[CoordinateCell, bool], None]) -> None:
        for cell in (self.battlefield.battlefield.get_cell(i) for i in range(self.battlefield.battlefield.size)):
            consumer(cell, self.is_free(cell))

    def _same_x(self, target: CoordinateCell) -> Iterator[CoordinateCell]:
        direction = -1 if self.source.y > target.y else 1
        for y in range(self.source.y + direction, target.y + direction, direction):
            yield self.battlefield.get_cell_by_coordinates(self.source.x, y)

    def _line(self, target: CoordinateCell) -> Iterator[CoordinateCell]:
        x_direction = -1 if self.source.x > target.x else 1
        y_direction = -1 if self.source.y > target.y else 1
        slope = (target.y - self.source.y) / (target.x - self.source.x)
        intercept = self.source.y - slope * self.source.x
        x, y = self.source.x, self.source.y
        y_at_x = (x + x_direction * 0.5) * slope + intercept
        rounded = floor(y_at_x + 0.5)
        next_y, last_y = (rounded, ceil(y_at_x - 0.5)) if y_direction > 0 else (ceil(y_at_x - 0.5), rounded)
        while (x, y) != (target.x, target.y):
            y += y_direction
            if y * y_direction > last_y * y_direction:
                x, y = x + x_direction, next_y
                y_at_x = (x + x_direction * 0.5) * slope + intercept
                rounded = floor(y_at_x + 0.5)
                next_y, last_y = (rounded, ceil(y_at_x - 0.5)) if y_direction > 0 else (ceil(y_at_x - 0.5), rounded)
            yield self.battlefield.get_cell_by_coordinates(x, y)
