"""
author: Peter Forgacs
date: 2013.11.13
use:Takes in a txt called protein_motif.txt and looks up the protein names in the txt on the  http://www.uniprot.org/
    looks up sequences and searches for N-glycosylation motifs prints out the name of the proteins that contain the
    motif and starting indexes in the sequence.

"""
import urllib2


def lose_slashn_list(x):
    removed = x.replace("\n", "")
    return removed
#Variable
z = 'a'
name_seq = []


#Megnyitni a a filet
#Beolvasni egy listbe
f = open('protein_motif.txt', 'r')  # Megnyitja a filet
l = f.readlines()  # Beolvassa a filet

#Bekuldi a lose_slasn - be a neveket
for i in range(len(l)):
    l[i] = lose_slashn_list(l[i])

#Megkeresni a szekvenciat az uniprot.org oldalrol es elmenti egy listbe l = [szekvencia , nev]
for i in range(len(l)):
    url = "http://www.uniprot.org/uniprot/"
    url_values= str(l[i]) + ".fasta"
    file_name = url  + url_values  #A neveket belerakja az URL-be
    file = urllib2.urlopen(file_name) #Megnyitja az URL-t
    z = str ((file.readlines()[1:])) #Beolvassa a filet es az elso sort kihagyva egy listbe teszi
    z = z.translate(None, "\\n" "," "'" " " "[" "]")
    name_seq.append(z)
    name_seq.append(l[i])

def sequence_search (x , q):
    if len(x) > 30:
        y = 0
        l = []
        counter = 0
        while y < len(x)-3:
            if (x[y] == "N") and (x[y+1] != "P") and (x[y+3] !="P") and  (x[y+2] == "S" or x[y+2] == "T"):
                y += 1
                l.append(y)
            else:
                y += 1
    printhatshit(l , q)

def printhatshit (l,q):
    if len(l) > 0:
        print name_seq[q+1]
        for i in range (len(l)):
            print l[i],
        print "\n"


i = 0
while i < len (name_seq):
    x = sequence_search (name_seq[i] , i)
    i += 2



