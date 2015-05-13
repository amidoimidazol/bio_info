__author__ = 'Peter'
t = "AAACCC"
s = "AAAGGG"
counter = 0
for i in range ( len(t)):
    if t[i] != s[i]:
        counter += 1
print counter
