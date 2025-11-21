# Using Iterative Division

n = 44
p = 1

for i in range(2, n + 1):
    if n % i == 0:
        res = True
        for j in range(2, int(i / 2) + 1):
            if i % j == 0:
                res = False
                break
        if res:
            p *= i

print(p)