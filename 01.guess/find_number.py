import random
import subprocess
import sys
import time
import datetime

message = ['The value is greater than your guess.\n', 'The value is less than your guess.\n']
result = message[0]

min = sys.maxint * (-1)
max = sys.maxint

start_time = time.time()
while result in message:
    num = random.randrange(min, max+1)
    print num
    result = subprocess.check_output('python __main__.pyc {}'.format(num), shell=True)
    if result==message[0]:
        min = num + 1
    else:
        max = num
end_time = time.time()



print "The hidden number is {}!".format(num)
print "Time to find the number takes {} seconds.".format(end_time - start_time)
