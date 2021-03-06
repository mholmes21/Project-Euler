# Read matrix into some variable
import csv
import numpy
import time
mat = numpy.array(list(csv.reader(open("p082_matrix.txt", "r"), delimiter=","))).astype("int")

# Initialize the min_path dictionary
min_path = {}
r = mat.shape[0]
c = mat.shape[1]

start = time.time()
for i in range(r):
    min_path[(i, c - 1)] = mat[i, c - 1]
#print(min_path)


# Main loop for calculating the path (in reverse)
for j in reversed(range(c-1)):

    for l in range(r):
        # initial values
        my_val = mat[l, j]
        min_path[(l, j)] = my_val + min_path[(l, j + 1)]

    for i in reversed(range(r)):
        values = list()
        my_val = mat[i, j]

        # "Top" edge
        if i == 0:
            for k in range(1, r):
                values.append(my_val + sum(mat[i+1:k+1, j]) + min_path[(i + k, j + 1)])

        # Bottom Edge
        elif i == r - 1:
            for k in range(0, r-1):
                values.append(my_val + sum(mat[k:i, j]) + min_path[(i - k, j + 1)])

        # General Case
        else:
            for k in range(r):
                if k < i:
                    values.append(my_val + sum(mat[k:i, j]) + min_path[(k, j + 1)])

                elif k > i:
                    values.append(my_val + sum(mat[i+1:k+1, j]) + min_path[(k, j + 1)])


        m = min(values)
        if m < min_path[(i, j)]:
            min_path[(i, j)] = m
        #print("(", i, ",", j, "):", min(values), min_path[(i, j)])


# Return the min of min_path([i, 0]) for i in [0,r]
actual_mins = list()
for i in range(r):
    actual_mins.append(min_path[(i, 0)])

print()
print("The min sum is", min(actual_mins))
print()
end = time.time()
print("that took", end-start, "seconds")

'''
for j in range(5):
    for i in range(5):
        print("(", i, ",", j, "):", min_path[(i, j)])
'''
