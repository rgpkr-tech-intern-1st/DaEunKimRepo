import unittest
import sys
import types
import find_number as fn


class TestCount(unittest.TestCase):
    """
    GIVEN:
    function 'find' searches for a number between two numbers.
    """
    def setUp(self):
        self.find = fn.find

    """
    WHEN:
    'count' returns result of 'find' and its running time as tuple.
    """
    def runTest(self):
        self.num, self.time_ = fn.count(self.find, -sys.maxint - 1, sys.maxint)

    """
    THEN:
    first element in tuple is an integer.
    second element in tuple is an float greater or equal to 0.
    """
    def assert_(self):
        self.assertIsInstance(self.num, types.IntType)
        self.assertIsInstance(self.time_, types.FloatType)
        self.assertTrue(self.time_ >= 0)


if __name__ == '__main__':
    unittest.main()
