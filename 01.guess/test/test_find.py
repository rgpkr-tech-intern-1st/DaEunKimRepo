import unittest
import sys
import find_number as fn


class TestFind(unittest.TestCase):
    """
    GIVEN:
    min_ is minimum of integer.
    max_ is maximum of integer.
    """
    def setUp(self):
        self.min_ = -sys.maxint - 1
        self.max_ = sys.maxint

    """
    WHEN:
    function 'find' searches for a number between min_ and max_.
    """
    def runTest(self):
        self.result = fn.find(self.min_, self.max_)

    """
    THEN:
    'find' returns 1954421783993232787.
    """
    def assert_(self):
        self.assertEqual(self.result, 1954421783993232787)


if __name__ == '__main__':
    unittest.main()
