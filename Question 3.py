#Created: Robert Morgan, 1/17/23
#Edited: Robert Morgan, 1/18/23
#Purpose: To find the prime factors of the number given

import math

userInput = 600851475143

number = userInput
currentNumber = userInput
factors = []
x = 1

while x <= currentNumber:

    if number % x == 0:

        z = x
        GCF = 1

        while currentNumber % z == 0:

            z = x*z
            factors.append(x)

            if x == 1:
                break

        for i in factors:
        
            GCF = GCF * i

        currentNumber = number/(GCF)

       
    if x == 1:
        x = x-1

    if x == 2:
         x = 1

    x += 2

factors = sorted(list(set(factors))) 

print(factors)