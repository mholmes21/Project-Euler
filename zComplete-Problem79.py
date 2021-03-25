# Problem 79: Passcode Derivation

## Read file into list called entries
f = open("p079_keylog.txt", "r")
entries = list()

for line in f:
    entries.append(int(line))

## Get rid of duplicate entries
u_entries = list(set(entries))
print(u_entries)

## Solved by hand
