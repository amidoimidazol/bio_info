'''

Author: Peter Chip (furamail001@gmail.com)

Date: 2015 03 23

Given: Positive integers n≤40 and k≤5.

Return: The total number of rabbit pairs that will be present after n months if we begin with 1 pair and in each generation, every pair of reproduction-age rabbits produces a litter of k rabbit pairs (instead of only 1 pair).

Theory: The standard fibonacci series : 1 1 2 3 5 8 13
        fn = fn-1 + fn-2
        In reality its fn = fn-1 + (fn-2)k where k is the number it gets incremeneted. In  the standard fibonacci set k is 1.

'''
#Setting up variables
n = 32
k = 5

# First three months
L = [1,2 + k-1]

# All the other months
i = 2
while i <= n-2:
    L.append(L[i-1]+ (L[i-2])*k)
    i += 1
print(L)

