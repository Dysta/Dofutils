from unittest import TestCase
from value.dimension import *

class TestDimension(TestCase):
    def test_dimension(self):
        dim: Dimension = Dimension(15, 17)

        self.assertEqual(15, dim.width())
        self.assertEqual(17, dim.height())

    def test_equals(self):
        dim: Dimension = Dimension(15, 17)

        self.assertEqual(dim, dim)

        self.assertNotEqual(dim, Dimension(13, 20))
        self.assertNotEqual(dim, Dimension(15, 20))
        self.assertNotEqual(dim, Dimension(10, 17))

        self.assertNotEqual(dim, None)
