class Interval:
    def __init__(self, min: int, max: int) -> None:
        if max < min:
            raise ValueError("max must be higher than min")

        self._min = min
        self._max = max

    def min(self) -> int:
        """
        Return the current min of the interval

        :return: The min of the interval
        :rtype: int
        """
        return self._min

    def max(self) -> int:
        """
        Return the current max of the interval

        :return: The max of the interval
        :rtype: int
        """
        return self._max

    def __contains__(self, value: int) -> bool:
        """
        Return True if the value is in the interval, false otherwise

        :param value: The value to check
        :return: True if the value is in, false otherwise
        :raise ValueError: If the value to check is not an integer
        :rtype: bool
        """
        if value.__class__ != int:
            raise ValueError("Value must be a integer")

        return self._min <= value <= self._max

    def modify(self, modifier: int) -> 'Interval':
        """
        Modify the end of the interval
        The returned interval will be [min, max + modifier]
        If the new end is lower than the min (i.e. -modifier higher than max - min), the interval [min, min] will be returned

        :param modifier: The modifier value. If positive will increase max, if negative will decrease
        :return: The new interval
        :rtype: Interval
        """
        if modifier == 0 or (self._min == self._max and modifier < 0):
            return self

        return Interval(self._min, max(self._max + modifier, self._min))

    def __eq__(self, other) -> bool:
        if self.__class__ != other.__class__:
            return False

        return self.min() == other.min() and self.max() == other.max()
