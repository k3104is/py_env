import random

inner = 0
N = 1000000

for _ in range(N):
    x = random.uniform(0, 1)
    y = random.uniform(0, 1)
    if (x**2 + y**2 <= 1):
        inner += 1

print(4 * inner / N)