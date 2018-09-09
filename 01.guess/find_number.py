import subprocess
import sys
import time


def find_by_binary_search(**args):
    min_ = args['min_']
    max_ = args['max_']
    while True:
        num = (min_ + max_) / 2
        print num
        result = subprocess.check_output(['python', 'guess.zip', str(num)])
        if 'greater' in result:
            min_ = num + 1
        elif 'less' in result:
            max_ = num - 1
        else:
            break
    return num


def count_seconds(function_, **args):
    start_time = time.time()
    yield function_(**args)
    end_time = time.time()
    yield end_time - start_time


if __name__ == '__main__':
    min_ = -sys.maxint - 1
    max_ = sys.maxint
    num, time_ = count_seconds(find_by_binary_search, min_=min_, max_=max_)
    print 'The hidden number is {0}!'.format(num)
    print 'It takes {0} seconds.'.format(time_)
