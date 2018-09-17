from behave import given, when, then
import sys
import find_number as fn


class TestFind():
    @given('min_ is minimum of integer.')
    def give_min(context):
        context.min_ = -sys.maxint - 1

    @given('max_ is maximum of integer.')
    def give_max(context):
        context.max_ = sys.maxint

    @when('`find` searches for a number between min_ and max_.')
    def when_execute(context):
        context.result = fn.find(context.min_, context.max_)

    @then('`find` returns 1954421783993232787.')
    def return_num(context):
        assert context.result == 1954421783993232787
