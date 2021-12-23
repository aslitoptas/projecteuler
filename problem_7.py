#!/bin/python3
#Solution of Problem 7 by Project Euler
#Finding the Nth prime number

import sys
import math

t = int(input().strip())
primes = [2,3]

for a0 in range(t):
    n = int(input().strip())
    if n > len(primes):
        if len(primes) == 2:
            a = 5
        elif (primes[len(primes) - 1] + 1) % 6 == 0:
            a = primes[len(primes) - 1] + 6
        else:
            a = primes[len(primes) - 1] + 4
        while(len(primes) < n):
            if any(a % x == 0 for x in primes[:]):
                pass
            else:
                primes.append(a)
            if any((a + 2) % x == 0 for x in primes[:]):
                pass
            else:
                primes.append(a + 2)
            a += 6
    else:
        pass
    print(primes[n-1])
