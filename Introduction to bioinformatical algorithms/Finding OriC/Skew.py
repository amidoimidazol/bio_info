s = " CATGGGCATCGGCCATACGCC"
prefix = s
a = ""

gc = 0
counter = 0
i = 0
while i < len(s):
    a += s[i]
    if s[i] == "G":
        gc += 1
    elif s[i] == "C":
        gc -= 1
    if i == prefix:
        a = ""
        gc = 0

    print gc,
    i += 1
    counter +=1

