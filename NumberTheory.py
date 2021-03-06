import copy
import fractions
import time
import math

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

# Returns a dictionary containing the prime factorization of n
def primeFactorization(n):
    N = n
    canon = {}

    # Check for factors of 2, the only even prime
    p = 2
    if n % p == 0:
        canon[p] = 1
        n //= p
    while n % p == 0:
        canon[p] += 1
        n //= p

    # Check for odd prime factors
    p = 3
    while p <= N:
        while n % p == 0:
            if p not in canon:
                canon[p] = 1
            else:
                canon[p] += 1
            n //= p
        p += 2

    return canon

# Returns list of all prime numbers less than n using a sieve.
# sieve[n] refers to the natural number n
def sievePrimeList(n):
    sieve = [True for x in range(n+1)]
    # 1 and 0 are defined to not be prime
    sieve[0] = False
    sieve[1] = False

    # Only check multiples for the first sqrt(n) values in the list
    for x in range(2, math.ceil(n**0.5)):
        # Exclude multiples of x
        for i in range(x, n, x):
            if i+x <= n:
                sieve[i+x] = False

    return sieve


# Returns Euler-Phi(n); how many #s < n are coprime to n
def totient(n):
    if n < 1:
        return -1
    canon = primeFactorization(n)
    primes = 1
    prime_num = 1
    for p in canon:
        primes *= p
        prime_num *= (p-1)
    return (n*prime_num)//primes


# Returns the digit sum of n
def digitSum(n):
    return sum([int(i) for i in str(n)])


# Returns the nth pentagonal number
def pentagonal(n):
    return n*(3*n - 1)//2


# Returns boolean if n is a pentagonal number or not
def isPentagonal(n):
    # Use Quadratic formula; check for int solutions
    if (((1 + math.sqrt(1 + 24*n))/6) % 1) == 0.0:
        return 1
    else:
        return 0


# Returns boolean if n in a triangular number or not
def isTriangular(n):
    # Use Quadtratic formula; check for int solutions
    if (-1 + math.sqrt(1 + 8*n))*0.5 % 1 == 0.0:
        return 1
    else:
        return 0


def isPermutation(x, y):
    # Determines if x & y are permutations of each other or not
    # First, if the lengths aren't equal, stop
    strx = str(x)
    stry = str(y)
    if len(strx) is not len(stry):
        return 0

    # If they are, turn them into strings and sort them
    strx = ''.join(sorted(strx))
    stry = ''.join(sorted(stry))

    x_prime = int(strx)
    y_prime = int(stry)

    # Then digit-wise subtract them
    ans = y_prime - x_prime

    # If the answer is 0, they're the same
    if ans == 0:
        return 1
    else:
        return 0
    # After this process, we'll have returned 1 if x and y are permutations; and returned 0 if they are not


def isPandigital(x):
    # Determines if x is pandigital
    #  that is, if x has N digits, x is N-pandigital if it has 0, 1, 2, ..., N represented
    # Only coded for 0-9 pandigital

    debug=0
    err = 0 # 0=pandigital; 1=length not 10; 2=repeated values
    number = list(str(x))
    length = len(number)
    if length is not 10:
        err = 1
        if debug:
            print(number, err)
        return 0
    else:
        # Sort the list to make our lives easier
        number.sort()

        # Remove 0-9 from the number
        for i in range(10):
            if str(i) in number:
                number.remove(str(i))

        # Check if there's anything left
        if number == []:
            if debug:
                print(number, err)
            return 1
        else:
            err = 2
            if debug:
                print(number, err)
            return 0


def get_divisors(n):
    divisors = [1, n]

    if n % 2 == 0:
        divisors.append(2)
        divisors.append(n//2)

    for x in range(3, math.ceil(math.sqrt(n+1)), 2):
        if n % x == 0:
            divisors.append(x)
            divisors.append(n//x)

    divisors.sort()

    return list(set(divisors))


def divisor_func(n, k):
    divisors = get_divisors(n)
    s = 0
    for d in divisors:
        s += d**k
    return s


def partition(n):
    if n == 0 or n == 1:
        return 1
    else:
        return int((1/n)*sum([divisor_func(n - k, 1)*partition(k) for k in range(0, n)]))


def mobius(n):
    if n == 1:
        return 1

    if n % 4 == 0:
        return -1

    k = 0
    for p in range(3, n, 2):
        if isPrime(p):
            if n % p == 0:
                k += 1
                if n % p **2 == 0:
                    return 0
    return (-1)**k
