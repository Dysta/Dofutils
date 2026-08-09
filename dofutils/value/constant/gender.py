from __future__ import annotations

from enum import IntEnum
from typing import Literal


class Gender(IntEnum):
    MALE = 0
    FEMALE = 1

    @staticmethod
    def parse(value: Literal["0", "1"]) -> Gender:
        """
        Get gender from string

        :param value: The string to parse
        :return: The Gender
        :rtype: Gender
        """
        val: int = int(value)
        try:
            return Gender(val)
        except ValueError:
            raise ValueError(f"Incorrect parameter {value}, must be 0 or 1")

    def __eq__(self, value: object) -> bool:
        """
        Check if the given value is equal to this gender

        :param value: The value to check
        :return: True if the value is equal, false otherwise
        :rtype: bool
        """
        return super().__eq__(value)

    def __str__(self) -> str:
        """
        Return the name of the gender as a string.

        :return: The name of the gender
        :rtype: str
        """
        return self.name
