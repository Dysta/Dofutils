from unittest import TestCase

from dofutils.maps.constant import Direction
from dofutils.maps.path import PathDecoder, PathException

from .._map import TestMap


class TestDecoder(TestCase):
    def setUp(self):
        self.map = TestMap()
        self.decoder = PathDecoder(self.map)

    def test_next_cell_by_direction(self):
        self.assertEqual(101, self.decoder.next_cell_by_direction(self.map.get_cell(100), Direction.EAST).id)
        self.assertIsNone(self.decoder.next_cell_by_direction(self.map.get_cell(470), Direction.SOUTH))

    def test_decode_and_encode(self):
        path = self.decoder.decode("ebIgbf", self.map.get_cell(100))
        self.assertEqual([100, 99, 98, 69], [step.cell.id for step in path])
        self.assertEqual("abKebIgbf", self.decoder.encode(path))
        self.assertEqual([100, 99, 98, 69], [step.cell.id for step in self.decoder.decode("abKebIgbf")])

    def test_invalid_path(self):
        with self.assertRaises((PathException, ValueError)):
            self.decoder.decode("abcd", self.map.get_cell(123))
