#Created: Robert Morgan, 1/16/23
#Edited: Robert Morgan, 1/16/23

import math

x = range(0,1000)

count = 0

for n in x:
    if (n % 3 == 0 or n % 5 ==0):
        count += n
print(count)
