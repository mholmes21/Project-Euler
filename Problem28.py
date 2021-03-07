# Initialize variables for NxN matrix
# Note: 1x1 sum = 1
i = 1
p_sum = 1
sum = 1
N = 1001

from time import time

# Recognize that each higher sum is the previous sum + the corners
# The top-right-most corner is always N^2; subtract N-1 on all edges

start = time()
while i < N:
    i += 2
    sum = p_sum + 4*i**2 - 6*i + 6
    p_sum = sum
end = time()

print ("Total for ", N, "x", N, ":", sum)
print ("That took ", end-start, "seconds")