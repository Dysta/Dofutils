from unittest import TestCase
from value.color import *


class TestColor(TestCase):
    def test_getters(self):
        c: Color = Color(123, 456, 789)

        self.assertEqual(123, c.color1())
        self.assertEqual(456, c.color2())
        self.assertEqual(789, c.color3())

    def test_colors(self):
        c: Color = Color(123, 456, 789)

        self.assertListEqual([123, 456, 789], c.colors())

    def test_hex_colors(self):
        c: Color = Color(123, 456, 789)

        self.assertListEqual(["7b", "1c8", "315"], c.hex_colors())

    def test_hex_color_str(self):
        c: Color = Color(123, 456, 789)

        self.assertEqual("7b;1c8;315", c.hex_color_str(";"))

    def test_default(self):
        c: Color = Color.default()

        self.assertEqual(-1, c.color1())
        self.assertEqual(-1, c.color2())
        self.assertEqual(-1, c.color3())

    def test_equals(self):
        c1: Color = Color(123, 456, 789)

        self.assertEqual(c1, c1)
        self.assertEqual(c1, Color(123, 456, 789))

        self.assertNotEqual(c1, Color.default())
        self.assertNotEqual(c1, None)

        self.assertNotEqual(c1, Color(124, 456, 789))
        self.assertNotEqual(c1, Color(123, 455, 789))
        self.assertNotEqual(c1, Color(123, 456, 788))

    def test_random(self):
        c: Color
        for _ in range(5000):
            c = Color.random()

            self.assertNotEqual(-1, c.color1())
            self.assertNotEqual(-1, c.color2())
            self.assertNotEqual(-1, c.color3())
