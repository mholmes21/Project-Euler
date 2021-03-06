from NumberTheory import get_divisors, divisor_func
import time
# 1, 2, 3, 4, 5, 6,  7,  8, ...
# 1, 1, 2, 3, 5, 7, 11, 15, 22, 30, 42, 56, 77, 101, 135
# 0, 1, 1, 2, 4, 6, 10, 14, 21, 29, 41, 55, 76, 100, 134

parts = {0: 1, 1: 1}


def partition(n):
    if n not in parts:
        parts[n] = int((1 / n) * sum([divisor_func(n - k, 1) * partition(k) for k in range(0, n)]))
    return parts[n]


print(partition(100))
print(parts)

parts2 = parts

for key in parts2:
    if key != 0 and key != 1:
        parts2[key] -= 1

print(parts2)