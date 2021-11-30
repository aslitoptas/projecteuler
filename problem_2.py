#!/bin/python3
#Solution of Problem 2 by Project Euler
#Finding the sum of all even Fibonacci numbers smaller than N

import sys


t = int(input().strip())

for a0 in range(t):
    n = int(input().strip())
    #Initialize for simplicity
    fibo=[1,2]
    fibo_even=[2]
    for i in range(1,n):
        new_element=fibo[i]+fibo[i-1]
        #Create the Fibonacci series
        if new_element>n:
            #Stop iterating new elements that will not be used
            break
        fibo.append(new_element)
        #Add the even numbered elements in a seperate list
        if new_element%2==0 and new_element<=n:
            fibo_even.append(new_element)
    #Print the sum of all elements in the list of even numbers
    print(sum(fibo_even))
