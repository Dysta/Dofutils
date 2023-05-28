from unittest import TestCase

from dofutils.maps.constant import Direction


class TestDirection(TestCase):
    def test_to_char(self):
        self.assertEqual("e", Direction.WEST.to_char())
        self.assertEqual("a", Direction.EAST.to_char())

    def test_by_char(self):
        self.assertEqual(Direction.WEST, Direction.by_char("e"))
        self.assertEqual(Direction.SOUTH, Direction.by_char("c"))

    def test_opposite(self):
        self.assertEqual(Direction.WEST, Direction.EAST.opposite())
        self.assertEqual(Direction.NORTH, Direction.SOUTH.opposite())

    def test_orthogonal(self):
        self.assertEqual(Direction.SOUTH, Direction.EAST.orthogonal())
        self.assertEqual(Direction.WEST, Direction.SOUTH.orthogonal())
        self.assertEqual(Direction.NORTH, Direction.WEST.orthogonal())
        self.assertEqual(Direction.EAST, Direction.NORTH.orthogonal())

    def test_restricted(self):
        self.assertFalse(Direction.WEST.restricted())
        self.assertFalse(Direction.NORTH.restricted())
        self.assertFalse(Direction.EAST.restricted())
        self.assertFalse(Direction.SOUTH.restricted())

        self.assertTrue(Direction.SOUTH_WEST.restricted())
        self.assertTrue(Direction.NORTH_WEST.restricted())
        self.assertTrue(Direction.NORTH_EAST.restricted())
        self.assertTrue(Direction.SOUTH_EAST.restricted())

    def test_next_cell_increment(self):
        self.assertEqual(1, Direction.EAST.next_cell_increment(15))
        self.assertEqual(15, Direction.SOUTH_EAST.next_cell_increment(15))
        self.assertEqual(29, Direction.SOUTH.next_cell_increment(15))
        self.assertEqual(14, Direction.SOUTH_WEST.next_cell_increment(15))

        self.assertEqual(-1, Direction.WEST.next_cell_increment(15))
        self.assertEqual(-15, Direction.NORTH_WEST.next_cell_increment(15))
        self.assertEqual(-29, Direction.NORTH.next_cell_increment(15))
        self.assertEqual(-14, Direction.NORTH_EAST.next_cell_increment(15))

    def test_restricted_directions(self):
        dirs: list = [
            Direction.SOUTH_EAST,
            Direction.SOUTH_WEST,
            Direction.NORTH_WEST,
            Direction.NORTH_EAST,
        ]
        self.assertListEqual(Direction.restricted_directions(), dirs)
