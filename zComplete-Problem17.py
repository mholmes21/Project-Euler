import math
import time

numbers = {1: 'one', 2: 'two', 3: 'three', 4: 'four', 5: 'five', 6: 'six', 7: 'seven', 8: 'eight',
           9: 'nine', 10: 'ten', 11: 'eleven', 12: 'twelve', 13: 'thirteen', 14: 'fourteen', 15: 'fifteen',
           16: 'sixteen', 17: 'seventeen', 18: 'eighteen', 19: 'nineteen', 20: 'twenty', 30: 'thirty', 40: 'forty',
           50: 'fifty', 60: 'sixty', 70: 'seventy', 80: 'eighty', 90: 'ninety', 100: 'onehundred', 200: 'twohundred',
           300: 'threehundred', 400: 'fourhundred', 500: 'fivehundred', 600: 'sixhundred', 700: 'sevenhundred',
           800: 'eighthundred', 900: 'ninehundred', 1000: 'onethousand'}


def two_dig(n):
    # assumes n is 2 digits
    if n <= 20:
        return numbers[n]
    elif n % 10 == 0:
        return numbers[n]
    else:
        x = (n // 10) * 10
        y = n % 10
        return numbers[x] + numbers[y]
    return 0


def three_dig(n):
    # assumes n is 3 digits
    if n % 100 == 0:
        return numbers[n]
    else:
        x = (n//100)*100
    return numbers[x] + 'and' + two_dig(n % 100)


def num2str(n):
    if n <= 20:
        # base numbers
        return numbers[n]
    elif math.log10(n) < 2:
        # two digit numbers
        return two_dig(n)
    elif math.log10(n) < 3:
        # three digit numbers
        return three_dig(n)
    else:
        # 1000 itself
        return numbers[n]

start = time.time()
N = 1000
count = 0
for i in range(1, N+1):
    count += len(num2str(i))
    #print(i, ":", num2str(i))
end = time.time()

print("There are", count, "many letters", (end-start)*1000, "ms")
print()