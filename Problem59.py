# XOR decryption; key is 3 lowercase ascii characters
# Decrypt the message, and return the sum of the decoded ascii

## Read file
f = open("p059_cipher.txt", "r")
#print(f.read())

## Ascii dict
asciiDict = {i: chr(i) for i in range(128)}

## Translate ascii to characters
myfile = f.readline()
mywords = myfile.split(',')

plain = list()

for word in mywords:
    plain.append(asciiDict[int(word)])
    
print(plain)
