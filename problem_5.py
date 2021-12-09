#!/bin/python3
#Solution of Problem 5 by Project Euler
#Finding the smallest number that is divisible by all numbers from 1 to N

import sys
import math

t = int(input().strip())
for a0 in range(t):
    n = int(input().strip())
    smallestMultiple = 1
    factors = list()
    for i in range(1, n+1):
        uniqueFactor = 1
        if smallestMultiple % i != 0:
            num = i
            for x in factors:
                if num % x == 0:
                    uniqueFactor = num // x
                    num = num // x
            if uniqueFactor == 1:
                factors.append(i)
                smallestMultiple *= i
            else:
                factors.append(uniqueFactor)
                smallestMultiple *= uniqueFactor
    print(smallestMultiple)