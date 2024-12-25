import unittest

from main import categorize


class TestKikiboba(unittest.TestCase):
    def test_categorize(self):
        self.assertEqual(categorize("boba"), "boba")
        self.assertEqual(categorize("kiki"), "kiki")
        self.assertEqual(categorize("kobra"), "boki")
        self.assertEqual(categorize("ljus"), "none")


if __name__ == '__main__':
    unittest.main()
