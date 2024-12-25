import unittest

from decimal import Decimal
from main import probability


class TestMonopol(unittest.TestCase):
    def test_probability(self):
        self.assertAlmostEqual(probability((7,)), Decimal(6/36), 4)
        self.assertAlmostEqual(probability((2, 12)), Decimal(2/36), 4)
        self.assertAlmostEqual(probability((
            2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12)), Decimal(36/36))


if __name__ == "__main__":
    unittest.main()
