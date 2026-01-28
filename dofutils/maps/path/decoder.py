from __future__ import annotations

from dataclasses import dataclass
from itertools import groupby
from typing import List, Optional

from dofutils.encoding import Base64
from dofutils.maps import CoordinateCell, DofusMap
from dofutils.maps.constant import Direction
from dofutils.maps.path import Path

from .path_exception import PathException
from .path_step import PathStep


@dataclass(frozen=True)
class PathDecoder:
    map: DofusMap

    def next_cell_by_direction(self, start: CoordinateCell, dir: Direction) -> Optional[CoordinateCell]:
        """
        Get the next cell on the map given a starting cell and a direction

        :param start: The starting cell
        :type start: AbstractMapCell
        :param dir: The direction
        :type dir: Direction
        :return: The next cell on the map, or None if the direction is invalid (out of map bounds)
        :rtype: Optional[AbstractMapCell]
        """
        next_id: int = start.id + dir.next_cell_increment(self.map.dimensions.width)

        if next_id < 0 or next_id >= self.map.size:
            return None

        return self.map.get_cell(next_id)

    def decode(self, encoded: str, start: Optional[CoordinateCell] = None) -> Path:
        """
        Decode a path encoded string into a list of directions

        :param encoded: The encoded path string
        :type encoded: str
        :param start: The starting cell, if None the first direction is considered absolute, defaults to None
        :type start: Optional[AbstractMapCell]
        :return: The list of directions
        :rtype: list[Direction]
        """
        if len(encoded) % 3 != 0:
            raise ValueError("Encoded path length must be a multiple of 3")

        directions: Path = Path(self)

        if start:
            directions += PathStep(start, Direction.EAST)

        for i, c in enumerate(encoded):
            if c < "a" or c > "h":
                raise ValueError(f"Invalid direction character: {c}")

            dire: Direction = Direction.by_char(c)
            cell: int = ((Base64.ord(encoded[i + 1]) & 15) << 6) + Base64.ord(encoded[i + 2])

            if cell >= self.map.size:
                raise ValueError(f"Invalid cell id: {cell}")

            if directions.empty():
                directions += PathStep(self.map.get_cell(cell), Direction.EAST)
                continue

            self._expand_rectilinear_move(directions, directions.target().cell, self.map.get_cell(cell), dire)

        return directions

    def encode(self, path: Path, include_start: bool = False) -> str:
        """
        Encode a path into a string

        :param path: The path to encode
        :type path: Path
        :param include_start: Whether to include the starting cell in the encoded string, defaults to False
        :type include_start: bool
        :return: The encoded path string
        :rtype: str
        """
        encoded: List[str] = []

        if include_start:
            encoded.append(Direction.EAST.to_char())
            encoded.append(Base64.encode(path.first().cell.id, 2))

        start: int = 0 if include_start else 1
        for direction, steps in groupby(path.steps[start:], lambda s: s.direction):
            steps = list(steps)

            encoded.append(direction.to_char())
            encoded.append(Base64.encode(steps[-1].cell.id, 2))

        return "".join(encoded)

    def _expand_rectilinear_move(
        self, path: Path, start: CoordinateCell, target: CoordinateCell, direction: Direction
    ) -> None:
        steps_limit: int = 2 * self.map.dimensions.width + 1

        while start != target:
            if (c := self.next_cell_by_direction(start, direction)) is None:
                raise PathException(f"Invalid cell number, cannot move from {start} to {target}")

            path += PathStep(c, direction)

        if steps_limit < 0:
            raise PathException(f"Invalid path, too many steps from {start} to {target}")

        steps_limit -= 1
