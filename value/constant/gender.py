from enum import IntEnum
from typing import Literal


class Gender(IntEnum):
    MALE = 0
    FEMALE = 1

    @staticmethod
    def parse(value: Literal["0", "1"]) -> 'Gender':
        """
        Get gender from string

        :param value: The string to parse
        :return: The Gender
        :rtype: int
        """
        if len(value) > 1:
            raise ValueError(f"Incorrect parameter {value}, must be 0 or 1")
        if "0" not in value and "1" not in value:
            raise ValueError(f"Incorrect parameter {value}, must be 0 or 1")

        if "0" in value:
            return Gender.MALE

        return Gender.FEMALE
