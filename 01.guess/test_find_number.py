import unittest
import find_number as fn
import sys
import types


class TestFindNumber(unittest.TestCase):
    min_ = -sys.maxint - 1
    max_ = sys.maxint

    def test_find(self):
        num = 1954421783993232787
        self.assertEqual(fn.find(TestFindNumber.min_, TestFindNumber.max_), num)

    def test_count(self):
        num, time_ = fn.count(fn.find, TestFindNumber.min_, TestFindNumber.max_)
        self.assertIsInstance(num, types.IntType)
        self.assertIsInstance(time_, types.FloatType)
        self.assertTrue(time_ >= 0)


if __name__ == '__main__':
    unittest.main()
