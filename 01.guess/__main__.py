# uncompyle6 version 3.2.3
# Python bytecode 2.7 (62211)
# Decompiled from: Python 2.7.10 (default, Oct  6 2017, 22:29:07) 
# [GCC 4.2.1 Compatible Apple LLVM 9.0.0 (clang-900.0.31)]
# Embedded file name: ./__main__.py
# Compiled at: 2018-03-16 16:34:42
from __future__ import print_function
import sys

def main(guess):
    n = 1954421783993232787
    if n < guess:
        print('The value is less than your guess.')
    else:
        if n > guess:
            print('The value is greater than your guess.')
        else:
            print('yay')


if __name__ == '__main__':
    if len(sys.argv) != 2:
        print(('Usage: python {} <number>').format(sys.argv[0]))
        sys.exit()
    try:
        guess = int(sys.argv[1])
    except ValueError:
        print('Please enter integer')
        sys.exit()

    main(guess)
# okay decompiling __main__.pyc
