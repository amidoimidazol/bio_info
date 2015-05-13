'''

Author: Peter Chip (furamail001@gmail.com)

Date: 2015 03 25

Given: Positive integers n≤100 and m≤20.

Return: The total number of pairs of rabbits that will remain after the n-th month if all rabbits live for m months.

Theory: The standard fibonacci series : 1 1 2 3 5 8 13
        fn = fn-1 + fn-2
        In reality its fn = fn-1 + (fn-2)k where k is the number it gets incremeneted. In  the standard fibonacci set k is 1.

        The number of pairs in the first six month
        m = 3 : 1 1 2 2 3 4
        m = 4 : 1 1 2 3 4 6
        m = 5 : 1 1 2 3 5 7

        After the first death the number of rabbits:
        fn = fn-2 + fn-3 ... fn-m
'''



def new_value(i):
    value = 0
    change = 2
    # Repeat it m - 1 times
    for y in range(1, m):
        # Add the fn-2 + fn-3 .. fn-m
        value += L[(i-change)]
        change += 1
    return value

# number of months
n = 94
# months a rabbit lives
m = 20


L = [1, 1, 2]
i = 3

while i < n:
    # If the first death occurs
    if i >= m:
        L.append(new_value(i))
        i += 1
    # If before the first death
    else:
        L.append(L[i-1]+ (L[i-2]))
        i += 1


print(L[len(L)-1])



