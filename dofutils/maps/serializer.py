from __future__ import annotations

from dataclasses import dataclass
from typing import Self

from dofutils.encoding import Base64, CheckSum, Key
from dofutils.maps.constant import CellMovement


@dataclass(frozen=True)
class CellLayerData:
    number: int = 0
    rotation: int = 0
    flip: bool = False

    @property
    def active(self) -> bool:
        return self.number != 0


@dataclass(frozen=True)
class GroundCellData(CellLayerData):
    level: int = 0
    slope: int = 0


@dataclass(frozen=True)
class InteractiveObjectData(CellLayerData):
    interactive: bool = False
    rotation: int = 0


@dataclass(frozen=True, slots=True)
class CellData:
    line_of_sight: bool
    movement: CellMovement
    active: bool
    ground: GroundCellData
    layer1: CellLayerData
    layer2: InteractiveObjectData


class DefaultMapDataSerializer:
    cell_data_length = 10

    def __init__(self) -> None:
        self._cache: dict[str, CellData] | None = None

    def enable_cache(self) -> Self:
        self._cache = {}
        return self

    def disable_cache(self) -> Self:
        self._cache = None
        return self

    def deserialize(self, map_data: str) -> list[CellData]:
        if len(map_data) % self.cell_data_length:
            raise ValueError("Invalid map data")

        return [self._deserialize_cell(map_data[i : i + 10]) for i in range(0, len(map_data), 10)]

    def serialize(self, cells: list[CellData]) -> str:
        return "".join(self._serialize_cell(cell) for cell in cells)

    def with_key(self, key: Key | str) -> EncryptedMapDataSerializer:
        return EncryptedMapDataSerializer(Key.parse(key) if isinstance(key, str) else key, self)

    def _deserialize_cell(self, value: str) -> CellData:
        if self._cache is not None and value in self._cache:
            return self._cache[value]

        d = Base64.to_bytes(value)
        cell = CellData(
            bool(d[0] & 1),
            CellMovement.by_value((d[2] & 56) >> 3),
            bool(d[0] & 32),
            GroundCellData(
                ((d[0] & 24) << 6) + ((d[2] & 7) << 6) + d[3],
                (d[1] & 48) >> 4,
                bool(d[4] & 2),
                d[1] & 15,
                (d[4] & 60) >> 2,
            ),
            CellLayerData(
                ((d[0] & 4) << 11) + ((d[4] & 1) << 12) + (d[5] << 6) + d[6], (d[7] & 48) >> 4, bool(d[7] & 8)
            ),
            InteractiveObjectData(
                ((d[0] & 2) << 12) + ((d[7] & 1) << 12) + (d[8] << 6) + d[9], 0, bool(d[7] & 4), bool(d[7] & 2)
            ),
        )

        if self._cache is not None:
            self._cache[value] = cell

        return cell

    @staticmethod
    def _serialize_cell(cell: CellData) -> str:
        d = [0] * 10
        d[0] = (
            (int(cell.active) << 5)
            | int(cell.line_of_sight)
            | ((cell.ground.number & 1536) >> 6)
            | ((cell.layer1.number & 8192) >> 11)
            | ((cell.layer2.number & 8192) >> 12)
        )
        d[1] = ((cell.ground.rotation & 3) << 4) | (cell.ground.level & 15)
        d[2] = ((cell.movement.value & 7) << 3) | ((cell.ground.number >> 6) & 7)
        d[3] = cell.ground.number & 63
        d[4] = ((cell.ground.slope & 15) << 2) | (int(cell.ground.flip) << 1) | ((cell.layer1.number >> 12) & 1)
        d[5], d[6] = (cell.layer1.number >> 6) & 63, cell.layer1.number & 63
        d[7] = (
            ((cell.layer1.rotation & 3) << 4)
            | (int(cell.layer1.flip) << 3)
            | (int(cell.layer2.flip) << 2)
            | (int(cell.layer2.interactive) << 1)
            | ((cell.layer2.number >> 12) & 1)
        )
        d[8], d[9] = (cell.layer2.number >> 6) & 63, cell.layer2.number & 63
        return "".join(Base64.chr(value) for value in d)


class EncryptedMapDataSerializer:
    def __init__(self, key: Key, serializer: DefaultMapDataSerializer | None = None):
        self.key, self.serializer = key, serializer or DefaultMapDataSerializer()

    def deserialize(self, map_data: str) -> list[CellData]:
        return self.serializer.deserialize(self.key.cipher.decrypt(map_data, CheckSum.integer(self.key.key) * 2))

    def serialize(self, cells: list[CellData]) -> str:
        return self.key.cipher.encrypt(self.serializer.serialize(cells), CheckSum.integer(self.key.key) * 2)
