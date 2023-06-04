from dataclasses import dataclass

from .abstract_map_cell import AbstractMapCell


@dataclass(frozen=True)
class BattleFieldCell(AbstractMapCell):
    sight_blocking: bool
    """Check if the cell block line of sight"""
