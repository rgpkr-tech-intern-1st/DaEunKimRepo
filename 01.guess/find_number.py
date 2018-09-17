# -*- coding: utf-8 -*-

"""
find()를 재귀로 구현했을 때 CC:

    F 26:0 find_with_recursive - A
    F 50:0 count - A

    2 blocks (classes, functions, methods) analyzed.
    Average complexity: A (2.0)

find()를 while문으로 구현했을 때 CC:

    F 37:0 find_with_loop - A
    F 50:0 count - A

    2 blocks (classes, functions, methods) analyzed.
    Average complexity: A (2.5)
"""

import subprocess
import sys
import time


def find_with_recursive(min_, max_):
    num = (min_ + max_) / 2
    result = subprocess.check_output(['python', 'guess.zip', str(num)])
    if 'greater' in result:
        return find_with_recursive(num + 1, max_)
    elif 'less' in result:
        return find_with_recursive(min_, num - 1)
    else:
        return num


def find_with_loop(min_, max_):
    while True:
        num = (min_ + max_) / 2
        result = subprocess.check_output(['python', 'guess.zip', str(num)])
        if 'greater' in result:
            min_ = num + 1
        elif 'less' in result:
            max_ = num - 1
        else:
            break
    return num


def count(func, min_, max_):
    start_time = time.time()
    num = func(min_, max_)
    end_time = time.time()
    return num, end_time - start_time


if __name__ == '__main__':
    min_ = -sys.maxint - 1
    max_ = sys.maxint

    num, time_ = count(find_with_recursive, min_, max_)
    print 'The hidden number is {}!'.format(num)
    print 'find_with_recursive takes {} seconds.'.format(time_)

    num, time_ = count(find_with_loop, min_, max_)
    print 'The hidden number is {}!'.format(num)
    print 'find_with_loop takes {} seconds.'.format(time_)

    print(__doc__)
