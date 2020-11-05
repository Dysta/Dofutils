from unittest import TestCase
from value.constant.race import *


class TestRace(TestCase):
    def test_by_id(self):
        for i in range(1, 13):
            self.assertEqual(Race(i), Race.by_id(i))
        self.assertRaises(ValueError, Race.by_id, race_id=0)
        self.assertRaises(ValueError, Race.by_id, race_id=13)
