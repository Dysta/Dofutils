from __future__ import annotations

from collections.abc import Callable
from dataclasses import dataclass, field
from itertools import takewhile
from typing import TYPE_CHECKING, overload

from .path_step import PathStep

if TYPE_CHECKING:
    from .decoder import PathDecoder


@dataclass
class Path:
    decoder: PathDecoder
    steps: list[PathStep] = field(default_factory=list)

    def path_step(self, index: int) -> PathStep:
        """
        Get a path step at a given index

        :param index: the index of the step to get
        :raises IndexError: if the index is out of range
        :return: the step at the given index
        :rtype: PathStep
        """
        if index < 0 or index >= len(self.steps):
            raise IndexError("Path step index out of range")

        return self.steps[index]

    def first(self) -> PathStep:
        """
        Get the first path step of the path

        :return: the first path step
        :rtype: PathStep
        """
        return self.path_step(0)

    def last(self) -> PathStep:
        """
        Get the last path step of the path

        :return: the last path step
        :rtype: PathStep
        """
        return self.path_step(len(self.steps) - 1)

    def target(self) -> PathStep:
        """
        Get the target path step of the path (the last step)

        :return: the target path step
        :rtype: PathStep
        """
        return self.last()

    def encode(self) -> str:
        """
        Encode the path into a string

        :return: The encoded path as a string
        :rtype: str
        """
        return self.decoder.encode(self)

    def keep_while(self, predicate: Callable[[PathStep], bool]) -> Path:
        """
        Keep the path steps while the predicate is true

        :param predicate: The predicate to apply to each path step
        :type predicate: callable[[PathStep], bool]
        :return: A new path with the kept steps
        :rtype: Path
        """
        return Path(self.decoder, list(takewhile(predicate, self.steps)))

    def empty(self) -> bool:
        """
        Check if the path is empty

        :return: True if the path is empty, false otherwise
        :rtype: bool
        """
        return len(self.steps) == 0

    def __len__(self) -> int:
        """
        Return the number of steps in the path

        :return: The number of steps
        :rtype: int
        """
        return len(self.steps)

    def __iter__(self):
        """
        Return an iterator over the path steps

        :return: An iterator over the path steps
        :rtype: Iterator[PathStep]
        """
        return iter(self.steps)

    @overload
    def __getitem__(self, index: int) -> PathStep: ...
    @overload
    def __getitem__(self, index: slice) -> list[PathStep]: ...

    def __getitem__(self, index: int | slice) -> PathStep | list[PathStep]:
        """
        Get a path step or a slice of path steps at a given index

        :param index: The index of the step or the slice to get
        :type index: Union[int, slice]
        :raises IndexError: if the index is out of range
        :return: The step or the slice of steps at the given index
        :rtype: Union[PathStep, List[PathStep]]
        """
        if isinstance(index, int):
            return self.path_step(index)
        elif isinstance(index, slice):
            return [self.path_step(i) for i in range(*index.indices(len(self)))]
        else:
            raise TypeError(f"Invalid argument type: {type(index)}")

    def __add__(self, other: Path | list[PathStep] | PathStep) -> Path:
        """
        Concatenate two paths together

        :param other: The other path to concatenate
        :type other: Union[Path, List[PathStep], PathStep]
        :return: A new path with all the steps of both paths
        :rtype: Path
        """
        if isinstance(other, list):
            return Path(self.decoder, self.steps + other)

        if isinstance(other, PathStep):
            return Path(self.decoder, self.steps + [other])

        return Path(self.decoder, self.steps + other.steps)
