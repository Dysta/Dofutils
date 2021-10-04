from unittest import TestCase
from dofutils.value.constant import Race


class TestRace(TestCase):
    def test_by_id(self):
        for i in range(1, 13):
            self.assertEqual(Race(i), Race.by_id(i))

    def test_by_id_wrong_param(self):
        self.assertRaises(ValueError, Race.by_id, race_id=0)
        self.assertRaises(ValueError, Race.by_id, race_id=13)
        self.assertRaises(ValueError, Race.by_id, race_id="5")
        self.assertRaises(ValueError, Race.by_id, race_id="95")
