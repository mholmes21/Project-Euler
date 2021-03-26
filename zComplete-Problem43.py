# Problem 43: find sum of pandigital 0-9 with weird divisibility properties
from NumberTheory import isPandigital
from itertools import permutations 
'''
count = 0
for k in range(1234567890, 10**10):
    print(k)
    if isPandigital(k, 0, 9):
        tmp = str(k)
        if int(tmp[1:4]) % 2 == 0 and int(tmp[2:5]) % 3 == 0 and int(tmp[3:6]) % 5 == 0 and int(tmp[4:7]) % 7 == 0 and int(tmp[5:8]) % 11 == 0 and int(tmp[6:9]) % 13 == 0 and int(tmp[7:10]) % 17 == 0:
            print("Success!")
            count += int(tmp)

print("The sum is", count)
'''

N = 10
count = 0
numbers = list()
for k in range(N):
    numbers.append(k)

#print(numbers)
p = permutations(numbers)
for j in list(p):
    tmp = str(int(''.join(map(str, j))))
    if int(tmp[1:4]) % 2 == 0 and int(tmp[2:5]) % 3 == 0 and int(tmp[3:6]) % 5 == 0 and int(tmp[4:7]) % 7 == 0 and int(tmp[5:8]) % 11 == 0 and int(tmp[6:9]) % 13 == 0 and int(tmp[7:10]) % 17 == 0:
            print("Success!")
            count += int(tmp)

print("The sum is", count)