import subprocess
import sys
import time


def find(min_, max_):
    num = (min_ + max_) / 2
    result = subprocess.check_output(['python', 'guess.zip', str(num)])
    if 'greater' in result:
        return find(num + 1, max_)
    elif 'less' in result:
        return find(min_, num - 1)
    else:
        return num


def count(func, min_, max_):
    start_time = time.time()
    num = func(min_, max_)
    end_time = time.time()
    return num, end_time - start_time


if __name__ == '__main__':
    min_ = -sys.maxint - 1
    max_ = sys.maxint
    num, time_ = count(find, min_, max_)
    print 'The hidden number is {}!'.format(num)
    print 'It takes {} seconds.'.format(time_)
