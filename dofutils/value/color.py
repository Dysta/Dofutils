from random import randint


class Color:
    _MAX_COLOR: int = 16777216

    def __init__(self, color1: int, color2: int, color3: int):
        self._color1 = color1
        self._color2 = color2
        self._color3 = color3

    def color1(self) -> int:
        """
        Return the first color

        :return: the first color
        :rtype: int
        """
        return self._color1

    def color2(self) -> int:
        """
        Return the second color

        :return: the second color
        :rtype: int
        """
        return self._color2

    def color3(self) -> int:
        """
        Return the third color

        :return: the third color
        :rtype: int
        """
        return self._color3

    def colors(self) -> list:
        """
        Return a list containing the colors

        :return: a list containing the color
        :rtype: list
        """
        return [self.color1(), self.color2(), self.color3()]

    def hex_colors(self) -> list:
        """
        Return a list containing the colors in a hexadecimal format

        :return: a list containing the color
        :rtype: list
        """
        return [hex(self.color1())[2:], hex(self.color2())[2:], hex(self.color3())[2:]]

    def hex_color_str(self, separator: str) -> str:
        """
        Return a str with the color joined by the separator

        :param separator: The separator between each color
        :return: A string containing the hexadecimal colors
        :rtype: str
        """
        return separator.join(self.hex_colors())

    def __eq__(self, other) -> bool:
        if self.__class__ != other.__class__:
            return False

        return (
            self.color1() == other.color1()
            and self.color2() == other.color2()
            and self.color3() == other.color3()
        )

    @staticmethod
    def default() -> "Color":
        """
        Return a object color with the default color
        -1 -1 -1

        :return: Return a default color
        :rtype: Color
        """
        return Color(-1, -1, -1)

    @staticmethod
    def random() -> "Color":
        """
        Return a object color with random color

        :return: Return a random color
        :rtype: Color
        """
        return Color(
            randint(0, Color._MAX_COLOR),
            randint(0, Color._MAX_COLOR),
            randint(0, Color._MAX_COLOR),
        )
