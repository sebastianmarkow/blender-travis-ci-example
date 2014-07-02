import unittest

from .. import add_one, add_two, add_number, subtract_number


class TestGeneral(unittest.TestCase):
    def setUp(self):
        pass

    def test_lib_add_one(self):
        """Should add 1 to an int"""
        r = add_one(5)
        self.assertEqual(r, 6)

    def test_lib_add_two(self):
        """Should add 2 to an int"""
        r = add_two(5)
        self.assertEqual(r, 7)

    def test_lib_add_number(self):
        """Should add up two int"""
        r = add_number(6, 7)
        self.assertEqual(r, 13)

    def test_lib_subtract_number(self):
        """Should subtract one int from another"""
        r = subtract_number(7, 6)
        self.assertEqual(r, 1)

    def tearDown(self):
        pass
