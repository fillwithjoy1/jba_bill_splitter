import unittest


def bounds(x):
    if x in range(50, 71):
        return x
    else:
        assert x in range(50, 70), "Your number is wrong!"


class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(bounds(60), 60)
