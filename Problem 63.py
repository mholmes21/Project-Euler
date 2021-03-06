import math
import time


start = time.time()
count_prev = 0
k = count = 1
while count != count_prev:
    for s in range(1, 10):
        count_prev = count
        if (1 - 1/k) < math.log10(s) and math.log(10, s) > 1:
            count += 1

    #print("Done with", k, "powers ...", "have", count, "k digit kth powers")
    k += 1

end = time.time()
print(count, "in ", end-start, "s")

# We need the following inequalities to be true:
# 10^(k-1) < s^k < 10^k
# take log10 of the left inequality, and logs of the right inequality for the conditional statement
