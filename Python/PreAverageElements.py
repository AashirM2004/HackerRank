#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'countResponseTimeRegressions' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER_ARRAY responseTimes as parameter.
#
# O(N) Time, O(1) Space

def countResponseTimeRegressions(responseTimes):
    # Write your code here
    if len(responseTimes) == 0:
        return 0
    runningTotal = responseTimes[0]
    i = 1
    count = 0
    while i < len(responseTimes):
        avg = runningTotal / i
        if responseTimes[i] > avg:
            count+= 1
        runningTotal+= responseTimes[i]
        i+= 1
    return count

if __name__ == '__main__':
    responseTimes_count = int(input().strip())

    responseTimes = []

    for _ in range(responseTimes_count):
        responseTimes_item = int(input().strip())
        responseTimes.append(responseTimes_item)

    result = countResponseTimeRegressions(responseTimes)

    print(result)
