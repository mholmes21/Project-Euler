import math


def add_digit_factorial(n):
    temp = 0
    for x in str(n):
        temp += math.factorial(int(x))

    return temp


def digit_factorial_chain(n):
    chain_results = {}
    L = 0
    tmp = n
    while tmp not in chain_results:
        chain_results[tmp] = 1
        L += 1
        tmp = add_digit_factorial(tmp)
    chain_results[tmp] = 1
    #print(chain_results)
    return L


N = 10**6
count = 0
for i in range(1, N):
    if digit_factorial_chain(i) == 60:
        print("Found one!", i)
        count += 1

print("Total:", count)
