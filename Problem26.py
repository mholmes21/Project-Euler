# Reciprocal Cycles
# Find the value of d < 1000 for which 1/d contains the longest recurring cycle in its decimal fraction part.

from time import time
from math import floor 


def recurring_substring_length(s):
    L = len(s)
    # The fewest number of repeating tiles is 2; so the biggest tile is half the string
    for i in range(1, floor(L/2 - 1) + 2):
        # Only check sub-strings whose lengths divide the length of the whole string
        tmp = s[0:i]
        l = len(tmp)
        print(tmp+tmp)
        print(s[0:2*l])
        print()
        if tmp+tmp == s[0:l]:
            print('win')
            
        
    # Otherwise, there's no pattern & return -1    
    return -1


# Initialize
N = 1000
d = 1
target = 1
max_d = 1

'''
start = time()
while d < N:
    # Save only the decimal part of 1/d
    d += 1
    x = 1/d
    suffix = str(x)
    suffix = suffix[2:]

    L = recurring_substring_length(suffix)
    print("d:", d, "length:", L)
    if L > target:
        target = L 
        max_d = d
        
end = time()

print("Max length:", L, "Max d:", d)
print("That took", end-start, "seconds")
print()
'''

x = str(1/7)
y = x[2:]
print(y)
print(recurring_substring_length(y))
