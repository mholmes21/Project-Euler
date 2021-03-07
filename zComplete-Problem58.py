import time


def isPrime(n):
    if n < 2:
        return 0
    elif n == 2:
        return 1
    elif n % 2 == 0:
        return 0
    else:
        for x in range(3, int(n**0.5) + 1, 2):
            if n % x == 0:
                return 0
    return 1


def calc_corners(s):
    tmp = list()
    tmp.append(s**2)
    tmp.append(s**2 - s + 1)
    tmp.append(s**2 - 2*s + 2)
    tmp.append(s**2 - 3*s + 3)
    return tmp


def count_primes(corners):
    tmp = [0]*len(corners)
    return sum([isPrime(x) for x in corners])


start = time.time()
# Start with side length 1
# Temp variable for counting number of primes
s = 1
p = 0
while (s):
    corners = calc_corners(s)
    p += count_primes(corners)
    s += 2
    # Check if #primes/#total is less than 10%
    if (s > 7) and (p/(2*s - 1) < 0.10):
        break
end = time.time()

print("The value of s is:", s, "in", end-start, "seconds")
