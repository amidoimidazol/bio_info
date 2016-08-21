__author__ = 'Peter'

def isitcool(x , y):
    if x == "A" and y == "T":
        return True
    elif x=="G" and y == "C":
        return True
    elif x=="C" and y == "G":
        return True
    elif x=="T" and y == "A":
        return True
    else:
        return False
# File beolvasasa es megnyitasa
f = open('reverse.txt', 'r').readlines()[1:]  # Megnyitja a filet
y = str(f)
y = y.translate(None, "\\n" "," "'" " " "[" "]")

l = []

i = 0
while i < (len(y)):
    norm4 = y[i] + y[i+1] + y[i+2] + y[i+3]
    rev4 = norm4[3] + norm4[2] + norm4[1] + norm4[0]
    counter = 0
    for x in range (3):
        var = isitcool (norm4[x],rev4[x])
        if var is True:
            counter += 1
            if counter == 3:
                q =str (i+1) + " " + "4"
                print q
    norm4 = norm4 + y[i+4] + y[i+5]
    rev4 = norm4[5] + norm4[4] + norm4[3] + norm4[2] + norm4[1] + norm4[0]
    counter = 0
    for x in range (5):
        var = isitcool (norm4[x],rev4[x])
        if var is True:
            counter += 1
            if counter == 5:
                q = str (i+1) + " " + "6"
                print q
    norm4 = norm4 + y[i+6] + y[i+7]
    rev4 = norm4[7] +norm4[6] +norm4[5] + norm4[4] + norm4[3] + norm4[2] + norm4[1] + norm4[0]
    counter = 0
    for x in range (7):
        var = isitcool (norm4[x],rev4[x])
        if var is True:
            counter += 1
            if counter == 7:
                q = str (i+1) + " " + "8"
                print q
    norm4 = norm4 + y[i+8] + y[i+9]
    rev4 = norm4[9] +norm4[8] +norm4[7] + norm4[6] +norm4[5] + norm4[4] + norm4[3] + norm4[2] + norm4[1] + norm4[0]
    counter = 0
    for x in range (9):
        var = isitcool (norm4[x],rev4[x])
        if var is True:
            counter += 1
            if counter == 9:
                q = str (i+1) + " " + "10"
                print q
    norm4 = norm4 + y[i+10] + y[i+11]
    rev4 = norm4[11] +norm4[10] +norm4[9] +norm4[8] +norm4[7] + norm4[6] +norm4[5] + norm4[4] + norm4[3] + norm4[2] + norm4[1] + norm4[0]
    counter = 0
    for x in range (11):
        var = isitcool (norm4[x],rev4[x])
        if var is True:
            counter += 1
            if counter == 11:
                q = str (i+1) + " " + "12"
                print q
    i += 1
print l