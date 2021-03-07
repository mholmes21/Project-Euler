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


def dig3_permutation(n):
    # Assumes triple is a list
    perms = list()
    a = str(n)[0]
    b = str(n)[1]
    c = str(n)[2]

    # Manually return the 6 permutations of 3 objects
    perms.append(int(a + b + c))
    perms.append(int(a + c + b))
    perms.append(int(b + a + c))
    perms.append(int(b + c + a))
    perms.append(int(c + a + b))
    perms.append(int(c + b + a))

    # perms is a list of 3-digit ints
    return perms


def dig4_permutation(n):
    perms = list()
    for c in str(n):
        if int(c) % 2 and int(c) != 5:
            tmp = dig3_permutation(str(n).replace(c, ''))
            #print("n:", n, ", c:", c, ", tmp:", tmp)
            adjusted = ["{}{}".format(x, c) for x in tmp]
            #print("adjusted:", adjusted)
            perms += adjusted

    return perms


def prime_dig4_perms(perms):
    primes = list()

    for x in perms:
        if isPrime(int(x)):
            primes.append(x)

    return primes


# Make a dictionary of possible combinations of digits
combinations = {}

# Loop over half of the odd 4 digit numbers
for i in range(1001, 5999, 2):
    # Not ending in 5
    if i % 10 != 5:
        # Not with any 0s in it
        if str(i).find('0') == -1:
            # Only the prime ones
            if len(''.join(set(str(i)))) == 4:
                if isPrime(i):
                    candidates = prime_dig4_perms(dig4_permutation(i))
                    digits = [int(y) for y in str(i)]
                    digits.sort()
                    if digits not in combinations and len(candidates) >= 3:
                        print("i:", i)
                        print(candidates)
                        combinations[repr(digits)] = candidates
                        print()

# next, i need to check the arithmetic progression for each of the candidates