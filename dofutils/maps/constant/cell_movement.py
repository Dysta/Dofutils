from enum import IntEnum


class CellMovement(IntEnum):
    NOT_WALKABLE = 0
    NOT_WALKABLE_INTERACTIVE = 1
    TRIGGER = 2
    LESS_WALKABLE = 3
    DEFAULT = 4
    PADDOCK = 5
    ROAD = 6
    MOST_WALKABLE = 7

    def walkable(self) -> bool:
        """
        Check if the current movement is for a walkable cell

        :return: True if the cell is walkable, false otherwise
        """
        return self.value > CellMovement.NOT_WALKABLE_INTERACTIVE.value

    @staticmethod
    def by_value(value: int) -> "CellMovement":
        """
        Get a cell movement by its value. Value must be in range [0-7]

        :param value: The movement id
        :return: The movement object
        :raise ValueError: When value is not in range [0-7]
        """
        if (
            not CellMovement.NOT_WALKABLE.value
            <= value
            <= CellMovement.MOST_WALKABLE.value
        ):
            raise ValueError(f"Incorrect parameter {value}, must be in range [0-7]")

        return CellMovement(value)
