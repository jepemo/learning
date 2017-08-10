nelems = int(input())
elems = input().split()

positive = 0
negative = 0
zeroes   = 0

for e in elems:
    if int(e) == 0:
        zeroes = zeroes + 1
    elif int(e) > 0:
        positive = positive + 1
    else:
        negative = negative + 1
        
print ('{:.3f}'.format(positive/float(nelems)))
print ('{:.3f}'.format(negative/float(nelems)))
print ('{:.3f}'.format(zeroes/float(nelems)))
