# Problem 43: find sum of pandigital 0-9 with weird divisibility properties
from NumberTheory import isPandigital

count = 0
for k in range(10**9, 10**10):
    if isPandigital(k, 0, 9):
        tmp = str(k)
        if int(tmp[1:4]) % 2 == 0 and int(tmp[2:5]) % 3 == 0 and int(tmp[3:6]) % 5 == 0 and int(tmp[4:7]) % 7 == 0 and int(tmp[5:8]) % 11 == 0 and int(tmp[6:9]) % 13 == 0 and int(tmp[7:10]) % 17 == 0:
            print("Success!")
            count += int(tmp)

print("The sum is", count)


