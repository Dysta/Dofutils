from enum import Enum


class Direction(Enum):
    EAST = (0, lambda width: 1)
    SOUTH_EAST = (1, lambda width: width)
    SOUTH = (2, lambda width: 2 * width - 1)
    SOUTH_WEST = (3, lambda width: width - 1)
    WEST = (4, lambda width: -1)
    NORTH_WEST = (5, lambda width: -width)
    NORTH = (6, lambda width: -(2 * width - 1))
    NORTH_EAST = (7, lambda width: -(width - 1))

    def _ordinal(self) -> int:
        """
        Get the ordinal of the enum

        :return: The ordinal
        :rtype: int
        """
        return self.value[0]

    def to_char(self) -> str:
        """
        Get the char value of the direction

        :return: The direction char value
        """
        return chr(self._ordinal() + ord("a"))

    @staticmethod
    def by_char(c: str) -> "Direction":
        """
        Get the direction by its char value

        :param c: The direction character value
        :return: The direction
        """
        dirs: list = [d for d in Direction]
        return dirs[ord(c) - ord("a")]

    def opposite(self) -> "Direction":
        """
        Get the opposite direction

        :return: The opposite direction
        :rtype: Direction
        """
        dirs: list = [d for d in Direction]
        return dirs[(self._ordinal() + 4) % 8]

    def orthogonal(self) -> "Direction":
        """
        Get the orthogonal direction

        :return: The orthogonal direction
        :rtype: Direction
        """
        dirs: list = [d for d in Direction]
        return dirs[(self._ordinal() + 2) % 8]

    def restricted(self) -> bool:
        """
        Check if the direction is restricted.
        A restricted direction can be used in fight, or by monsters's sprites
        Restricted direction do not allow diagonal

        :return: True if the direction can be used when restrictions are enabled
        """
        return self.value[0] % 2 == 1

    def next_cell_increment(self, width: int) -> int:
        """
        Get the increment to apply to cell id for get the next cell on the direction

        :param width: The map width
        :return: The next cell id increment
        :rtype: int
        """
        return self.value[1](width)

    @staticmethod
    def restricted_directions() -> list:
        """
        Get the restricted direction (i.e can be used on fight)

        :return: A list of restricted direction
        :rtype: list
        """
        restricted: list = []
        for d in Direction:
            if d.restricted():
                restricted.append(d)

        return restricted
