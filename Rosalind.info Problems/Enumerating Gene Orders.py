n = 3
l = range (1,n+1)
eredeti = l
# Ez lesz az n-kitevoje
kozep = range ( 1,n) # n - 1
veg = range (1,len(l)-1) # N-1

for n in range (len(l)):    # n

    for z in kozep:
        # eredeti elso elemet beteszi elore
        for x in veg:
            l.insert(len(l)-2,l[len(l)- 1]) # n-1 tol N-2 ig
            del (l[len(l)-1])
            print l
