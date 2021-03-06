import time

start = time.time()
L = 5
cubes = {}
for i in range(1, 10**L):
    c = i**3
    k = ''.join(sorted(str(c)))
    if k not in cubes:
        cubes[k] = [i]
    else:
        cubes[k].append(i)

        if len(cubes[k]) == L:
            print("The first cube with", L, "permutations is", cubes[k])
            print(cubes[k][0], int(cubes[k][0])**3)
            break


end = time.time()
print("that took", end-start, "seconds")