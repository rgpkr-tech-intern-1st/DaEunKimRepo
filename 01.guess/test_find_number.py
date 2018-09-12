import unittest
import sys
import types
import find_number as fn


class TestFindNumber(unittest.TestCase):
    def test_find_should_return_True_when_range_and_answer_are_given(self):
        # GIVEN:
        # min_ is minimum of integer.
        # max_ is maximum of integer.
        # answer is 1954421783993232787.
        min_ = -sys.maxint - 1
        max_ = sys.maxint
        answer = 1954421783993232787

        # WHEN:
        # call 'find' with min_ and max_ as searching range.
        result = fn.find(min_, max_)

        # THEN:
        # it should return True when the result is equal to the answer.
        self.assertTrue(result, answer)

    def test_count_should_return_True_when_range_and_function_are_given(self):
        # GIVEN:
        # min_ is minimum of integer.
        # max_ is maximum of integer.
        # find is a function that searches answer between min_ and max_.
        min_ = -sys.maxint - 1
        max_ = sys.maxint
        find = fn.find

        # WHEN:
        # call 'count' with find, min_, and max_.
        num, time_ = fn.count(find, min_, max_)

        # THEN:
        # it should return find's result as integer.
        # it should return find's running time as float greater or equal to 0.
        self.assertIsInstance(num, types.IntType)
        self.assertIsInstance(time_, types.FloatType)
        self.assertTrue(time_ >= 0)


if __name__ == '__main__':
    unittest.main()
