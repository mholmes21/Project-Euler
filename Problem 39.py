# If p is the perimeter of a right angle triangle with integral length sides, {a,b,c}, there are exactly three solutions for p = 120.
#{20,48,52}, {24,45,51}, {30,40,50}
# For which value of p ≤ 1000, is the number of solutions maximised?

# Set maximum bound
N = 100
i = 1
#print("Here's the first few pythagorean triples")

p = 200
perimeters = list()

for y in range(N):
    for x in range(y+1, N):

        new_x = (x+1)**2 - (y+1)**2
        new_y = 2*(x+1)*(y+1)
        new_z = (x+1)**2 + (y+1)**2
        #print("i:", i, "(", new_x, ",", new_y, ",", new_z, ")")
        i+=1

        tmp = new_x + new_y + new_z

        if new_x > p or new_y > p or new_z > p:
            #print("Failed attempt with:", tmp)
            continue
        else:
            if tmp == 120:
                print("Success with;", new_x, new_y, new_z)
            perimeters.append(tmp)


perimeters.sort()
print("")
print(perimeters)