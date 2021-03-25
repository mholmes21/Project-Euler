import fractions, math

## Make a loop that generates the sqrt(2) based on number of loops

def numerator_greater_denominator(loop):
    x = 0.5
    for i in range(loop):
        tmp = 2 + x
        x = 1/tmp

    #print((tmp - 1))
  
    ## Figure out number of digits in denominator
    f = fractions.Fraction(tmp-1).limit_denominator()
    n = repr(f.numerator)
    d = repr(f.denominator)
    print(n, d)  

    if len(str(n)) > len(str(d)):
        return 1
    else:
        return 0

N = 1000
count = 0
for x in range(N):
    count += numerator_greater_denominator(x+1)

print(count)
