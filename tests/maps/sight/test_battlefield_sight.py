from unittest import TestCase

from dofutils.maps.sight import BattlefieldSight

from .._map import TestMap


class TestBattlefieldSight(TestCase):
    def setUp(self):
        self.map = TestMap()
        self.sight = BattlefieldSight(self.map)

    def test_between(self):
        for source, target in ((177, 210), (210, 177), (241, 242), (137, 112), (126, 123), (123, 126), (156, 226)):
            self.assertTrue(self.sight.between(self.map.get_cell(source), self.map.get_cell(target)))
        for source, target in ((177, 146), (146, 177), (241, 243), (127, 169)):
            self.assertFalse(self.sight.between(self.map.get_cell(source), self.map.get_cell(target)))

    def test_line_cells(self):
        self.assertEqual([178, 163, 177, 162, 147], [cell.id for cell in self.sight.from_cell(self.map.get_cell(193)).to(self.map.get_cell(147))])
        self.assertEqual([181, 182, 183, 184, 185], [cell.id for cell in self.sight.from_cell(self.map.get_cell(180)).to(self.map.get_cell(185))])
