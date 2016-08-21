def lose_slashn_list(x):
    removed = x.replace("\n", "")
    return removed

f = open('ripping_test.txt', 'r')  # Megnyitja a filet
l = f.readlines()  # Beolvassa a filet

for i in range(len(l)):
    l[i] = lose_slashn_list(l[i])

print l