import math, time
N = 1000
scores = dict()

start = time.time()
for p in range(6, N+1, 2):
    count = 0
    for a in range(1, p//2):
        for b in range(1, a):
            c = math.sqrt(a**2 + b**2)
            if a+b+c == p:
                count += 1
    if count != 0:
        scores.update({p: count})
        #print(p, count)

print(max(scores, key=scores.get))
end = time.time()

print(end-start, "seconds")
