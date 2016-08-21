"""
author: Peter Forgacs
date: 2013.11.13
use:Input fasta szekvenciak amikben megkeresi hogy az elso nukleotid megegyezik-e az utolsa harommal , a parokat
    megkeresi es graphvizzal grafolhato directed grapha alakitje

"""
#Megnyitni a a filet
#Beolvasni egy listbe
f = open('overlap_graph.txt', 'r')  # Megnyitja a filet
l = f.read()  # Beolvassa a filet
l = l.split('>')  # Szetvagja listre a > jelnel
l.pop(0)  # Kiszedi a splittel keletkezo ures elemet a 0 helyrol


def lose_slashn_list(x):
    removed = x.replace("\n", "")
    return removed
# Soronkent stringkent bekuldi hogy kivegyek a \n-t es aztan visszarakja listbe
for i in range(len(l)):
    l[i] = lose_slashn_list(l[i])
u = []
d = {}

#Vegigloopolni a listen es bekuldi az elso harom nukletidot ha az megegyezik az utolso harommal listbe rakja
for i in range(len(l)):
    utolso_harom = l[i][len(l[i])-3:]
    for z in range(len(l)):
        if utolso_harom == l[z][13:16]:
            if l[i] != l[z]:
                u.append(l[i][:13])
                u.append(l[z][:13])

i = 0
#Graphviz formatumba konvertalja a listet es kiprinteli
while i < len(u)-1:
    n = str(u[i]) + " -> " + str(u[i+1])
    print(n)
    i += 2
