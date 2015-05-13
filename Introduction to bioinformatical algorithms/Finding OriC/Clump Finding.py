import timeit

start = timeit.default_timer()
k = 9
L = 500
t = 3
s = open('E-coli.txt','r').readlines()


def search_k (string):
    counter = 0
    loc = []
    for i in range (len(s[0])-(k-1)):
        looking_for = s[0][i:i+k]
        if string == looking_for and counter < t:
            counter += 1
            loc.append(i)
            print loc
        if counter == t:
            if int (loc[0]+L+1) >= loc[t-1]:
                return True
    return False

l = []
counter = 0
for i in range (len(s[0])-(k-1)):
    code = s[0][i:i+k]
    print i
    if code not in l:
        l.append (code)
        number_of_repetition = search_k(code)
        if number_of_repetition == True:
            print s[0][i:i+k],
            counter += 1

print counter
stop = timeit.default_timer()

print stop - start
