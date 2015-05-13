"""
__author__ = 'Peter Forgacs'
gc.txt filebol beolvas FASTA szekvenciakat aztan megkeresi azt amelyiknek a legnagyobb a GC tartalma
"""
# DEFINITIONS


# Input egy string amiben megszamolja a G es C ket Output egy list ami [nev,GCszama,teljes string hossz]
def fasta_to_dic(x):
    gc = 0
    i = 0
    while i < len(x)-13:
        if x[i+13] == "G":
            gc += 1
            i += 1
            d = [str(x[0:13]), gc, len(x)-13]
        elif x[i+13] == "C":
            gc += 1
            i += 1
            d = [str (x[0:13]), gc, len(x)-13]
        else:
            i += 1
    return d


#Input list aminek az elemei listek , Output a darabszambol atlagot szamol
def number_to_percent(x):
    for i in range(len(x)):
        n = float(x[i][2])/float(100)
        x[i][1] = (x[i][1] / n)

    return x

#Input String kiszedi a \n-t es stringkent visszakuldi
def lose_slashn_list(x):
    removed = x.replace("\n", "")
    return removed


f = open('gc.txt', 'r')  # Megnyitja a filet
l = f.read()  # Beolvassa a filet
l = l.split('>')  # Szetvagja listre a > jelnel
l.pop(0)  #Kiszedi a splittel keletkezo ures elemet a 0 helyrol

#Variables
gc = 0
total = ["a", 1]
i = 1
d = []
gc = 0
o = 0
z = []

# Soronkent stringkent bekuldi hogy kivegyek a \n-t es aztan visszarakja listbe
for i in range (len(l)):
    l[i] = lose_slashn_list(l[i])

#Elkuldi a list elemeit  a fasta_to_dic-be
for i in range(len(l)):
    y = l[i]
    z.append(fasta_to_dic(y))
#Elkuldi a number to percentbe
zig = number_to_percent(z)

#Kivalasztja a legnagyobb erteket
for i in range(len(zig)):
    if zig[i][1] > total[1]:
        total[0] = zig[i][0]
        total[1] = zig[i][1]
#Print
print total[0]
print total[1]


