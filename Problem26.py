# Reciprocal Cycles
# Find the value of d < 1000 for which 1/d contains the longest recurring cycle in its decimal fraction part.

from time import time
#from numpy import uint32

N = 1000
i = 1

start = time()
while i < N:
    i += 1
    d = 1/i
    print("1 /", i, "=", d)
end = time()

print("That took", end-start, "seconds")


