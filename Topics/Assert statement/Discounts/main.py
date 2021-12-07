import unittest


def discounts(x, y):
    if y * 2 < x:
        return "I will buy it!"
    else:
        assert y * 2 < x


class MainTests(unittest.TestCase):
    def test_one(self):
        self.assertEqual(discounts(12, 5), "I will buy it!")

    def test_two(self):
        self.assertRaises(AssertionError, discounts(12, 7))
