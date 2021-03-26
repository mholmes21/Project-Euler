# Problem 75: How many values of L <= 1.5M have exactly 1 integer sideded right triangle?

## Definitions
import math
def number_right_triangles(side):
    count = 0
    for a in range(1, math.floor(side/2) + 1):
        for b in range(1, a+1):
            tmp = math.sqrt(a**2 + b**2)
            if tmp == side - a - b:
                count += 1
                if count > 1:
                    return -1
    
    return count


def fast_number_right_triangles(side):
    count = 0
    for n in range(1, math.floor(side/2) + 1):
        for m in range(n, math.floor(side/2) + 1):
            x = m**2
            y = n**2
            a = m*n 
            b = (x - y)/2
            c = (x + y)/2

            if a + b + c == side:
                count += 1 
                if count > 1:
                    return -1
    return count

#L = 1500000
L = 1500
count = 0
triangle_lengths = list()
for l in range(1, L+1):
    tmp = fast_number_right_triangles(l)
    #print("l,count:", l, tmp)
    if tmp == 1:
        count += 1
        triangle_lengths.append(l)

print("There are", count, "such lengths less than", L)

