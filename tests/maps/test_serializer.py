from unittest import TestCase

from dofutils.maps import CellData, CellLayerData, DefaultMapDataSerializer, GroundCellData, InteractiveObjectData
from dofutils.maps.constant import CellMovement


class TestSerializer(TestCase):
    def test_round_trip(self):
        cell = CellData(True, CellMovement.DEFAULT, True, GroundCellData(123, 2, True, 4, 5), CellLayerData(456, 3, True), InteractiveObjectData(789, 0, False, True))
        serializer = DefaultMapDataSerializer()
        self.assertEqual([cell], serializer.deserialize(serializer.serialize([cell])))
