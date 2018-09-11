from behave import given, when, then
import sys
import types
import find_number as fn


class TestCount():

    @given('function `find` searches for a number between two numbers.')
    def give_func(context):
        context.find = fn.find

    @when('`count` returns result of `find` and its running time as tuple.')
    def when_execute(context):
        num, time_ = fn.count(context.find, -sys.maxint - 1, sys.maxint)
        context.num = num
        context.time_ = time_

    @then('first element in tuple is an integer.')
    def check_first(context):
        assert isinstance(context.num, types.IntType)

    @then('second element in tuple is an float greater or equal to 0.')
    def check_second(context):
        assert isinstance(context.time_, types.FloatType)
        assert context.time_ >= 0
