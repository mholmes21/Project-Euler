import time


def add_digit_squares(n):
    tmp = 0
    for s in str(n):
        tmp += int(s)**2
    return tmp


def digit_square_chain(n):
    if n == 89:
        return 1
    elif n == 1:
        return 0
    else:
        return digit_square_chain(add_digit_squares(n))


N = 10**7
count = 0
start = time.time()
for x in range(1, N + 1):
    count += digit_square_chain(x)
end = time.time()

print("The number that stop at 89 is", count, "in", end-start, "seconds")

