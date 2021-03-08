from abc import ABC
from typing import TypeVar, Generic

T = TypeVar('T')


class DofusMap(ABC, Generic[T]):
    pass
