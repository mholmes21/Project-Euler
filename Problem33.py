from collections import Counter

def gcd(a, b):
    if b == 0:
        return a
    else:
        return gcd(b, a%b)


def digits_in_common(a, b):
    # Returns 1 if there are any digits in common in a and b
    str_a = Counter(str(a))
    str_b = Counter(str(b))

    common = str_a & str_b
    if len(common) == 0:
        return 0
    else:
        return list(common.elements())



for y in range(11, 100):
    for x in range(10, y):
        if x != y:
            g = gcd(x, y)
            if g > 1:
                commons = digits_in_common(x, y)
                if commons:
                    if (x % 10 != 0) and (y % 10 != 0):
                        c = commons[0]
                        if str(x//g) == str(x).replace(c, '') and str(y//g) == str(y).replace(c, ''):
                            print(x, y)