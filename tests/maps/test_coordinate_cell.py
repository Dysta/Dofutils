from unittest import TestCase

from dofutils.maps.constant import Direction

from ._map import TestMap


class TestCoordinateCell(TestCase):
    def setUp(self):
        self.map = TestMap()

    def test_coordinates_distance_and_direction(self):
        cell = self.map.get_cell(157)
        self.assertEqual((17, -7), (cell.x, cell.y))
        self.assertEqual(5, cell.distance(self.map.get_cell(227)))
        self.assertEqual(Direction.SOUTH_WEST, cell.direction_to(self.map.get_cell(227)))
        self.assertEqual(Direction.NORTH_EAST, cell.direction_to(self.map.get_cell(129)))
        self.assertEqual(Direction.SOUTH_EAST, cell.direction_to(self.map.get_cell(217)))
        self.assertEqual(Direction.NORTH_WEST, cell.direction_to(self.map.get_cell(67)))
