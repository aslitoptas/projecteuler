#!/bin/python3
#Solution of Problem 3 by Project Euler
#Finding the largest prime factor of N

import sys
import math

t = int(input().strip())
for a0 in range(t):
    n = int(input().strip())
    lprimef=1
    if n%2==0:
        while(n%2==0 and n>1):
            n = n/2
        lprimef=2
    if n%3==0:
        while(n%3==0 and n>1):
            n = n/3
        lprimef=3
    a = 5
    if n%a==0 and a**2>n: #Only for numbers below 25
        lprimef=5
    while(a**2<=n):
        if n%a==0:
            while(n%a==0 and n>1):
                n = n/a
            lprimef=a
        if n%(a+2)==0:
            while(n%(a+2)==0 and n>1):
                n = n/(a+2)
            lprimef=a+2
        a = a+6
    # Above loop can't calculate its largest prime factor if it is squarefree
    # Then final n will be the largest prime factor
    if n!=1:
        lprimef=int(n) #Final n is a float, so converting it back to integer
    print(lprimef)
