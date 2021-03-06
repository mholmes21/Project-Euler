import fractions, math


def root_2_approx(i):
    # Calculates the root2 convergence to term i
    tmp = 0
    divs = i
    while divs:
        divs -= 1
        d = 2 + tmp
        f = 1/d
        tmp = f
    return 1 + f


N = 10**2
count = 0
for x in range(1, N):
    print(format(root_2_approx(x), '.16g'))

