from unittest import TestCase

from dofutils.maps.constant import Direction
from dofutils.maps.path import PathDecoder

from .._map import TestMap


class TestPathfinder(TestCase):
    def setUp(self):
        self.map = TestMap()
        self.pathfinder = PathDecoder(self.map).pathfinder()

    def test_paths(self):
        self.assertEqual([123], [step.cell.id for step in self.pathfinder.find_path(self.map.get_cell(123), self.map.get_cell(123))])
        self.assertEqual([336, 322], [step.cell.id for step in self.pathfinder.find_path(self.map.get_cell(336), self.map.get_cell(322))])
        self.assertEqual([305, 291, 277, 263, 249, 235, 221], [step.cell.id for step in self.pathfinder.find_path(self.map.get_cell(305), self.map.get_cell(221))])
        self.assertEqual([169, 183, 168, 153, 139], [step.cell.id for step in self.pathfinder.find_path(self.map.get_cell(169), self.map.get_cell(139))])
        self.assertEqual([169, 168, 139], [step.cell.id for step in self.pathfinder.with_directions(Direction).find_path(self.map.get_cell(169), self.map.get_cell(139))])
