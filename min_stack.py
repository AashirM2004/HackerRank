#!/bin/python3

import math
import os
import random
import re
import sys



#
# Complete the 'processCouponStackOperations' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts STRING_ARRAY operations as parameter.
#

def processCouponStackOperations(operations):
    stack = []
    min_stack = []
    res = []
    
    for operation in operations:
        parts = operation.split()
        
        if parts[0] == "push":
            value = int(parts[1])
            stack.append(value)
            
            if not min_stack or value <= min_stack[-1]:
                min_stack.append(value)
        
        elif parts[0] == "pop":
            value = stack.pop()
            
            if value == min_stack[-1]:
                min_stack.pop()
                
        elif parts[0] == "top":
            res.append(stack[-1])
        
        elif parts[0] == "getMin":
            res.append(min_stack[-1])
            
    return res

if __name__ == '__main__':
    operations_count = int(input().strip())

    operations = []

    for _ in range(operations_count):
        operations_item = input()
        operations.append(operations_item)

    result = processCouponStackOperations(operations)

    print('\n'.join(map(str, result)))
