import unittest

from main import reduplicate


class TestReduplikation(unittest.TestCase):
    def test_reduplicate(self):
        self.assertEqual(reduplicate("hej", 3), "hejhejhej")
        self.assertEqual(reduplicate("ha", 4), "hahahaha")


if __name__ == '__main__':
    unittest.main()
