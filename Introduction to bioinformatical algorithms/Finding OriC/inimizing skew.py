s = " TAAAGACTGCCGAGAGGCCAACACGAGTGCTAGAACGAGGGGCGTAAACGCGGGTCCGAT"
a = ""
gc = 0
lowest = [-1]

for x in range (3,len(s)):
    i = 0
    a = ""
    while i < len(s):
        a += s[i]
        if s[i] == "G":
            gc += 1
        if s[i] == "C":
            gc -= 1
        if i % x == 0:
            if gc <= lowest[len(lowest)-1]:
                lowest.append(gc)
                print "x" ,x
            a = ""
            gc = 0

        i += 1


print "lowest" ,lowest
