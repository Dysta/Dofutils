class Dimension:
    def __init__(self, width: int, height: int) -> None:
        self._width = width
        self._height = height

    def width(self) -> int:
        """
        Return the width of the dimension

        :return: The width
        :rtype: int
        """
        return self._width

    def height(self) -> int:
        """
        Return the height of the dimension

        :return: The height
        :rtype: int
        """
        return self._height

    def __eq__(self, other) -> bool:
        if other.__class__ != self.__class__:
            return False

        return self.width() == other.width() and self.height() == other.height()
