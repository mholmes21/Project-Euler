# Problem 38: What is the largest 1 to 9 pandigital 9-digit number that can be formed as the concatenated product of an integer with (1,2, ... , n) where n > 1?
from NumberTheory import isPandigital
N = 10**4 
biggest = -1

## Outer loop decides k in k*(1, 2, ..., n); need to check all of them
for k in range(1, N+1):
    #print()
    #print("K:", k)

    ## Middle loop picks n in k*(1, 2, ..., n); need to try all bigger than 1
    for n in range(2, N+1):
        tmp = ''

        ## Inner loop actually compiles the concatenation for each endpoint
        for y in range(1, n+1):
            tmp += str(k*y)
        
        ## If 0 in any number, break out of inner loop; we only care about 1->9
        if '0' in tmp:
            break

        ## Need to check if the result is pandigital, and keep track of max
        tmp = int(tmp)
        
        #print(tmp)
        if isPandigital(tmp, 9) and tmp > biggest:
            biggest = tmp
            print("Update!", biggest)
    
    

print("The biggest is", biggest)

