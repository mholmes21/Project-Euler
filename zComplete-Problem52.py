# Problem  52: Find the smallest positive integer, x, such that 2x, 3x, 4x, 5x, and 6x, contain the same digits.
from time import time

# Function to check if the digits between inputs x and y are the same or not
def same_digits(x, y):
    
    if len(str(x)) != len(str(y)):
        return 0
    
    a = list(str(x))
    b = list(str(y))
    a.sort()
    b.sort()

    if a != b:
        return 0

    return 1

## Check 2x 3x 4x 5x 6x have the same digits
i = 1
start = time()
while(1):
    if same_digits(i, 2*i) and same_digits(i, 3*i) and same_digits(i, 4*i) and same_digits(i, 5*i) and same_digits(i, 6*i):
        print("Found!", i)
        break
    i += 1
    #print("i:", i)
end = time()

print("time:", end-start)