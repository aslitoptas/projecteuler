#!/bin/python3
#Solution of Problem 1 by Project Euler
#Finding the sum of all the multiplies of 3 or 5 below N

import sys


while(True):
    try:
        t = int(input().strip())
        if t>10**5 or t<1:
            print('Constraint error. Must be between 1 to 10^5. Try again.')
            continue
        break
    except:
        print('Invalid input.')
        continue

for a0 in range(t):
    try:
        n = int(input().strip())
        if n>=1 and n<=10**9:
            sum0 = 0
            range3=(n-1)//3
            range5=(n-1)//5
            range15=(n-1)//15
            multi3=(range3*(range3+1)) >> 1
            multi5=(range5*(range5+1)) >> 1
            multi15=(range15*(range15+1)) >> 1
            #Division then conversion to integer causes calculation error for very big numbers
            #Even when done after calculating the sum
            sum0=3*multi3+5*multi5-15*multi15
            print(sum0)
        else:
            print('Constraint error.')
    except:
        print('Invalid input.')
