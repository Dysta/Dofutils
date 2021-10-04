from unittest import TestCase
from dofutils.value.constant import Gender


class TestGender(TestCase):
    def test_parse(self):
        self.assertEqual(Gender.MALE, Gender.parse("0"))
        self.assertEqual(Gender.FEMALE, Gender.parse("1"))

    def test_parse_wrong_param(self):
        self.assertRaises(ValueError, Gender.parse, value=5)
        self.assertRaises(ValueError, Gender.parse, value="5")
        self.assertRaises(ValueError, Gender.parse, value="95")
