from unittest import TestCase
from dofutils.maps.constant import CellMovement


class TestCellMovement(TestCase):
    def test_walkable(self):
        self.assertFalse(CellMovement.NOT_WALKABLE.walkable())
        self.assertFalse(CellMovement.NOT_WALKABLE_INTERACTIVE.walkable())
        self.assertTrue(CellMovement.TRIGGER.walkable())
        self.assertTrue(CellMovement.LESS_WALKABLE.walkable())
        self.assertTrue(CellMovement.DEFAULT.walkable())
        self.assertTrue(CellMovement.PADDOCK.walkable())
        self.assertTrue(CellMovement.ROAD.walkable())
        self.assertTrue(CellMovement.MOST_WALKABLE.walkable())

    def test_by_value(self):
        for i in range(8):
            self.assertEqual(CellMovement(i), CellMovement.by_value(i))
