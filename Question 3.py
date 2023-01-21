#Created: Robert Morgan, 1/17/23
#Edited: Robert Morgan, 1/18/23

import math

number = 600851475143
currentNumber = 600851475143
x = 2
factors = []

while x <= currentNumber:

    if number % x == 0:

        z = x
        GCF = 1

        while currentNumber % z == 0:

            z = x*z
            factors.append(x)

# I want to iterate over the vector factors
        for i in factors:
        
            GCF = GCF * i

        currentNumber = number/(GCF)
        
    x += 1

factors = sorted(list(set(factors))) 

print(factors)