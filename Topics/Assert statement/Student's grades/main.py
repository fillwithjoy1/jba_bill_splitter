import unittest


def grades(x):
    if x in ('A', 'B', 'C', 'D', 'F'):
        return f"You have got {x}"
    else:
        assert x in ('A', 'B', 'C', 'D', 'F')


class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(grades('A'), "You have got A")
