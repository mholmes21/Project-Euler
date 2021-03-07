from NumberTheory import totient, primeFactorization, isPrime
import sys
import time
import math


def phi(m):
    # modified for only odds
    result = m
    p = 3
    while p**2 <= m:
        if m % p == 0:
            while m % p == 0:
                m /= p
            result -= result / p

        p += 2

    if m > 1:
        result -= result / m

    return int(result)

e = 3
N = 10**7
seen = {}
seen[1] = 1
min_r = sys.maxsize
min_n = sys.maxsize
start = time.time()

'''
for n in range(3, N, 2):
    t = phi(n)
    ns = sorted(str(n))
    ts = sorted(str(t))
    k = int(''.join(ns))

    if (ns == ts) and (k not in seen.keys()):
        r = n / t
        if r < min_r:
            min_r = r
            min_n = n
            seen[k] = 1
            now = time.time()
            print("New minimum!!!", n, "after", (now - start)/60, "minutes")


print("The value of n with minimal ratio is", min_n)
# The above method is too slow; I'm trying to find a faster way
'''


bound = math.floor(math.sqrt(N)) + 1
if bound % 2 == 0:
    d = 10**e + 1
else:
    d = 10**e

for p in range(3, bound + d, 2):
    if isPrime(p):
        for q in range(p + 2, bound + d, 2):
            if isPrime(q):

                n = p*q
                t = (p-1)*(q-1)
                if n > N:
                    break

                if sorted(str(n)) == sorted(str(t)):
                    r = n/t
                    if r < min_r:
                        min_r = r
                        min_n = n
                        #print("New min!!!", min_n, p, q)

end = time.time()
print()
print("the value of n which minimizes n/phi(n) is:", min_n, "in ", end-start, "seconds")