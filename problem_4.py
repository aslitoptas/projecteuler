#!/bin/python3
#Solution of Problem 4 by Project Euler
#Finding the largest palindrome product of two 3-digit numbers smaller than N

#I am sure there are much more easier ways to find the solution.

import sys

def is_divisible(number):
    #6 digit palindromes are divisible by 11, so one of those has to be a product of 11
    factor = 979
    while (factor >= 121):
        if number%factor == 0 and number/factor < 1000:
            return True
        else:
            factor -= 11

t = int(input().strip())

for a0 in range(t):

    n = int(input().strip())
    
    if n > 101101 and n < 1000000:
        pStr = str(n//1000)
        nCheck = n % 1000
        
        #Check the last 3 digits of N to create the largest palindrome smaller than N
        if int(pStr[::-1]) >= nCheck:
            pStr = str((n//1000 - 1))
        pStr = pStr + pStr[::-1]
        p0 = int(pStr)
        
        while(True):
            pStr = str(p0)
            if is_divisible(p0):
                largestPalindrome = p0
                break
            else:
            #Calculating the next palindrome according to digits of the previous one
            #So there will be less iterations
                if int(pStr[1:3]) == 0:
                    p0 -= 11
                elif int(pStr[2]) == 0:
                    p0 -= 110
                else:
                    p0 -= 1100  
        
        print(largestPalindrome)
