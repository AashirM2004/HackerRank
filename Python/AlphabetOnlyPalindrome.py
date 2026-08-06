#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'isAlphabeticPalindrome' function below.
#
# The function is expected to return a BOOLEAN.
# The function accepts STRING code as parameter.
#

def isAlphabeticPalindrome(code):
    newStr = ""
    for char in code:
        if char.isalpha():
            newStr += char
    lowerStr = newStr.lower()
    
    
    return lowerStr == lowerStr[::-1]

if __name__ == '__main__':
    code = input()

    result = isAlphabeticPalindrome(code)

    print(int(result))
