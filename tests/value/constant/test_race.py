from unittest import TestCase
from value.constant.race import *


class TestRace(TestCase):
    def test_by_id(self):
        self.assertEqual(Race.ECAFLIP, Race.by_id(6))
        self.assertRaises(ValueError, Race.by_id, race_id=0)
        self.assertRaises(ValueError, Race.by_id, race_id=13)
