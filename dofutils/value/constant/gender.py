from enum import IntEnum
from typing import Literal


class Gender(IntEnum):
    MALE = 0
    FEMALE = 1

    @staticmethod
    def parse(value: Literal["0", "1"]) -> "Gender":
        """
        Get gender from string

        :param value: The string to parse
        :return: The Gender
        :rtype: Gender
        """
        val: int = int(value)
        if val not in list(map(int, Gender)):
            raise ValueError(f"Incorrect parameter {value}, must be 0 or 1")

        return Gender(val)
