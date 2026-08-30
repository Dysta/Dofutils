from __future__ import annotations

import heapq
from collections.abc import Callable, Iterable
from itertools import count
from typing import Self

from dofutils.maps.constant import Direction
from dofutils.maps.coordinate_cell import CoordinateCell

from .decoder import PathDecoder
from .path import Path
from .path_exception import PathException
from .path_step import PathStep


class Pathfinder:
    def __init__(self, decoder: PathDecoder):
        self.decoder = decoder
        self._target_distance = 0
        self._walkable_predicate: Callable[[CoordinateCell], bool] = lambda cell: cell.walkable
        self._cell_weight: Callable[[CoordinateCell], int] = lambda cell: 1
        self._directions: Iterable[Direction] = Direction.restricted_directions()
        self._explored_cell_limit = float("inf")
        self._add_first_cell = True

    def target_distance(self, distance: int) -> Self:
        self._target_distance = distance
        return self

    def walkable_predicate(self, predicate: Callable[[CoordinateCell], bool]) -> Self:
        self._walkable_predicate = predicate
        return self

    def cell_weight_function(self, function: Callable[[CoordinateCell], int]) -> Self:
        self._cell_weight = function
        return self

    def with_directions(self, directions: Iterable[Direction]) -> Self:
        self._directions = directions
        return self

    def explored_cell_limit(self, limit: int) -> Self:
        self._explored_cell_limit = limit
        return self

    def include_first_cell(self, include: bool) -> Self:
        self._add_first_cell = include
        return self

    def find_path(self, source: CoordinateCell, target: CoordinateCell) -> Path:
        queue: list = []
        order = count()
        heapq.heappush(queue, (source.distance(target), 0, next(order), source, Direction.EAST, None))
        best, explored = {source.id: 0}, set()

        while queue:
            _, cost, _, cell, direction, previous = heapq.heappop(queue)
            if cell.id in explored:
                continue
            explored.add(cell.id)
            if len(explored) > self._explored_cell_limit:
                raise PathException("Limit exceeded for finding path")
            if cell.distance(target) <= self._target_distance:
                steps = []
                while previous is not None:
                    steps.append(PathStep(cell, direction))
                    cell, direction, previous = previous
                steps.reverse()
                if self._add_first_cell:
                    steps.insert(0, PathStep(source, Direction.EAST))
                return Path(self.decoder, steps)
            for new_direction in self._directions:
                adjacent = self.decoder.next_cell_by_direction(cell, new_direction)
                if adjacent is None or adjacent.id in explored or not self._walkable_predicate(adjacent):
                    continue
                new_cost = cost + self._cell_weight(adjacent)
                if new_cost < best.get(adjacent.id, float("inf")):
                    best[adjacent.id] = new_cost
                    state = (cell, direction, previous)
                    heapq.heappush(
                        queue,
                        (new_cost + adjacent.distance(target), new_cost, next(order), adjacent, new_direction, state),
                    )
        raise PathException(f"Cannot find any valid path between {source.id} and {target.id}")
