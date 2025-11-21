# Using Math Module
import math
n = 44
p = 1

if n % 2 == 0:
    p *= 2
    while n % 2 == 0:
        n //= 2

for i in range(3, int(math.sqrt(n)) + 1, 2):
    if n % i == 0:
        p *= i
        while n % i == 0:
            n //= i

if n > 2:
    p *= n
print(p)