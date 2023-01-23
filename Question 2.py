#Created: Robert Morgan, 1/16/23
#Edited: Robert Morgan, 1/16/23

import math

fib_1 = 0
fib_2 = 1
total = 0
fibCount = 0
upperBound = 4*pow(10,6)

while fib_1 < upperBound:
    if (fib_1 + fib_2) % 2 == 0:
        total += fib_1 +fib_2
    
    fibCount = fib_1 +fib_2
    fib_1 = fib_2
    fib_2 = fibCount
    
print(total)