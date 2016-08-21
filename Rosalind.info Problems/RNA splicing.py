"""
Given: A DNA string s (of length at most 1 kbp) and a collection of substrings of s acting as introns. All strings are given in FASTA format.

Return: A protein string resulting from transcribing and translating the exons of s. (Note: Only one solution will exist for the dataset provided.)
"""
# Open file
f = open('sample.txt','r').readlines()
l = [i.replace('\n', '') for i in f]


# Determine the length of the sequence
def len_seq(l):
    counter = 0
    l.remove(l[0])
    for i in range (len (l)):
        if l[i][0] == ">":
            counter +=1
        if counter == 1:
            return i
# Join sequence
s = ""
for i in range (0,len_seq(l)):
    s += str (l[0])
    l.remove(l[0])

# Remove names
for i in l:
    print i
    if i[0] == ">":
        l.remove(i)
#Insert back sequence
l.insert(0,s)

# Cut out introns
for i in range (1,len(l)):
    l = [q.replace(l[i], '') for q in l]


# Replace Timin with  Uracil
l = [q.replace("T", 'U') for q in l]


# Translate RNA to Protein
f = open ('codon.txt','r') #Megnyitja a filet

#Variablek
x = f.read()
d = {}
y = len (x)
s = str(l[0])
z = ""
print s

x = x.split("\n")                       # Beolvasott stringet listbe alak?tja

for i in range(len(x)):                 # Hatvannegyszer ismeteld meg
    if x[i][4:8] == 'Stop':             #Ha stop kodon van akkor tobb karakter szed ki
        d [x [i][0:3]] = x[i][4:8]      # Szedd ki a list i -edik elemenek 0:3 karakteret es ez lesz a dictionary value
    else:
        d [x [i][0:3]] = x[i][4:5]

i = 0
while i < len(s):
    z = z + d[s[i:i+3]]                 # z hez adja a d-ben lev? szekvenciahoz tartozo valuet (s-b?l definialva)
    i = i + 3                           #3-asaval ugral

print z
