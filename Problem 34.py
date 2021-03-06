from functools import reduce
from math import floor, log10
from time import time


def four_digit_nonzero():
    numbers = list()
    for i in range(1234, 9876 + 1):
        if '0' not in str(i):
            numbers.append(i)
    return numbers


def factor(n):
    factors = list(set(reduce(list.__add__, ([i, n//i] for i in range(1, int(n**0.5) + 1) if n % i == 0))))
    factors.sort()
    return factors


def special_factor_pairs(n):
    factors = factor(n)
    i = 0
    j = len(factors) - 1
    specials = list()

    # In general this is wrong, but in this case, square numbers aren't pandigital, so we're saving time
    while i < j:

        dig1 = floor(log10(factors[i]) + 1)
        dig2 = floor(log10(factors[j]) + 1)

        if (dig1 == 1 and dig2 == 4) or (dig1 == 2 and dig2 == 3):
            specials.append([factors[i], factors[j]])

        i += 1
        j -= 1

    return specials


def isPandigital(x):
    # Determines if x is pandigital
    #  that is, if x has 9 digits, x is 9-pandigital if it has 1, 1, 2, ..., 9 represented
    # Only coded for 1-9 pandigital

    debug=0
    err = 0 # 0=pandigital; 1=length not 10; 2=repeated values
    number = list(str(x))
    length = len(number)
    if length is not 9:
        err = 1
        if debug:
            print(number, err)
        return 0
    else:
        # Sort the list to make our lives easier
        number.sort()

        # Remove 0-9 from the number
        for i in range(1, 9+1):
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


def convert_product(in_list):
    # this function assumes the list has 2 elements
    if len(in_list) != 2:
        print("ERROR!!! LIST HAS WRONG SIZE")
        return -1

    x = in_list[0]
    y = in_list[1]

    z = x*y

    ans = int(str(x) + str(y) + str(z))

    return ans


def problem_32():
    print("Getting list of all 4 digit numbers without 0...")
    numbers = four_digit_nonzero()
    print("Done!")
    print("")
    master_list = list()

    print("Factor those numbers, and find special pairs!")
    for x in range(len(numbers)):
        specials = special_factor_pairs(numbers[x])

        # Check each 4 digit number's special pairs
        for y in range(len(specials)):
            if isPandigital(convert_product(specials[y])):
                master_list.append(reduce(lambda a, b: a*b, specials[y]))

    print("Done!")

    print(sum(set(master_list)))

    return 0

start = time()
problem_32()
end = time()

print(end-start, "seconds")