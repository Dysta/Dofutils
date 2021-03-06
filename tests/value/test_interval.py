from unittest import TestCase
from value.interval import *


class TestInterval(TestCase):
    def test_bad_init(self):
        self.assertRaises(ValueError, Interval, min=5, max=2)

    def test_min(self):
        inter: Interval = Interval(2, 5)

        self.assertEqual(2, inter.min())

    def test_max(self):
        inter: Interval = Interval(2, 5)

        self.assertEqual(5, inter.max())

    def test_contains(self):
        inter: Interval = Interval(5, 15)

        self.assertRaises(ValueError, inter.__contains__, value="yo")

        self.assertTrue(10 in inter)
        self.assertTrue(5 in inter)
        self.assertTrue(15 in inter)

        self.assertFalse(20 in inter)
        self.assertFalse(4 in inter)

    def test_modify(self):
        inter: Interval = Interval(5, 10)

        self.assertEqual(inter, inter.modify(0))
        self.assertEqual(Interval(5, 15), inter.modify(5))
        self.assertEqual(Interval(5, 7), inter.modify(-3))
        self.assertEqual(Interval(5, 5), inter.modify(-10))

        inter = Interval(5, 5)

        self.assertEqual(inter, inter.modify(-2))
        self.assertEqual(Interval(5, 7), inter.modify(2))

    def test_equals(self):
        self.assertEqual(
            Interval(5, 7),
            Interval(5, 7)
        )

        self.assertNotEqual(
            Interval(5, 7),
            Interval(4, 6)
        )

        self.assertNotEqual(
            Interval(4, 7),
            Interval(5, 7)
        )

        self.assertNotEqual(
            Interval(5, 7),
            Interval(5, 9)
        )

    def test_average(self):
        self.assertEqual(12.5, Interval(10, 15).average())

    def test_amplitude(self):
        self.assertEqual(
            5,
            Interval(10, 15).amplitude()
        )

        self.assertEqual(
            0,
            Interval(10, 10).amplitude()
        )

        self.assertEqual(
            20,
            Interval(0, 20).amplitude()
        )

        self.assertEqual(
            15,
            Interval(-20, -5).amplitude()
        )
