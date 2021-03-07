# Lychel #s

def isPalindrome(n):
    # Returns if a number is a palindrome or not
    str1 = [int(d) for d in str(n)]
    length = len(str1)
    i = 0
    j = length - 1
    while i < j:
        if str1[i] is not str1[j]:
            return 0
        i += 1
        j -= 1
    return 1

#print(isPalindrome(122))

def lychelSum(n):
    # Returns the sum of the input number n and it's reverse
    tmp = [int(d) for d in str(n)]
    tmp.reverse()
    s = map(str, tmp)
    s = ''.join(s)
    reversed_number = int(s)
    return n + reversed_number


N = 10000
limit = 50
lychel_numbers = list()

# Check each number in the range 1 -> N
for x in range(N):
    flag = 0
    print("Checking", x+1, "now ...")
    tmp = x + 1
    # Run the Lychel Sum a max of limit (50) times; need to find a way to update this in a loop x = x + 1
    for i in range(limit):
        tmp = lychelSum(tmp)

        # Break if we find a Palindrome, and set the flag
        if isPalindrome(tmp):
            flag = 1
            break

    # Count the numbers that didn't reach a Palindrome
    if flag == 0:
        lychel_numbers.append(x+1)

print("")
print("There are", len(lychel_numbers), "Lychel Numbers <", N)