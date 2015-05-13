from itertools import permutations

#generates all possible permutations and saves them as a list
x = list(map("".join, permutations('1234')))

#prints
for i in range(len(x)):
    print x[i]