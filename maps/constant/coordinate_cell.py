from typing import TypeVar, Generic

C = TypeVar('C')


class CoordinateCell(Generic[C]):
    def __init__(self, cell: C):
        self._cell: C = cell

        width: int = cell.map().dimensions().width()
        line: int = cell.id() / (width * 2 - 1)
        column: int = cell.id() - line * (width * 2 - 1)
        offset: int = column % width

        self._y: int = line - offset
        self._x: int = (cell.id() - (width - 1) * self._y) / width
