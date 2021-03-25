# Problem 72: how many elements contained in proper fractions with d <= 1,000,000?

from NumberTheory import totient
from time import time

## Set max value
N = 1000000
count = 0
progress = 1

## Add up all phi(n) for values >= denominator; that will give us # fractions that dont reduce
start = time()
for i in range(2, N+1):
    t = totient(i)
    count += t
    #print("i,t:",i,t)
    if i == 10**progress:
        print("We've reached", 10**progress)
        progress += 1
end = time()
print("There are", count, "proper fractions")
print(end-start)