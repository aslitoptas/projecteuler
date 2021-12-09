#!/bin/python3
#Solution of Problem 6 by Project Euler
#Absolute difference between the sum of the squares and the square of the sum

t = int(input().strip())
for a0 in range(t):
    n = int(input().strip())
    sumofSquares = (n * (n + 1) * (2*n + 1)) // 6
    squareofSums = (n * (n + 1) // 2) ** 2
    sumSquareDif = abs(squareofSums - sumofSquares)
    print(sumSquareDif)