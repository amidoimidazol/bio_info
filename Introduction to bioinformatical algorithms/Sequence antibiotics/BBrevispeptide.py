"""
Author: Peter Forgacs

Date: 2014.03.14

Description: Searches for a peptide coding sequence in Bacillus Brevis genome and prints out the number of it.

Question: Is that peptide present in the Bacillus Brevis genome? (all 6 reading frames)

"""

#Setting up variables
protein = "WKLFPWFNEY"
dnacomplement = []
counter = 0

#Open up the list with the codons
f = open('codon2.txt', 'r')
l = f.readlines()
#Open up the Bacillus Brevis genom
dna = open('B_brevis.txt','r').read()


#Function that gets the complement of a dna sequence
def complement (x):
    for i in range(len(x)):
        if x[i] == "G":
            dnacomplement.append('C')
        elif x[i] == "C":
            dnacomplement.append('G')
        elif x[i] == "A":
            dnacomplement.append('T')
        elif x[i] == "T":
            dnacomplement.append('A')


#Searches for codons 5'-> 3' and the complement strand in 5'->3'
#Go trough every possible codon all 3 reading frames.
for i in range (len(dna)-1):
    codon = dna[i:i + len(protein)*3]

    #Get the reverse complement
    dnacomplement = []
    complement(codon)
    x = ""
    x = "".join(dnacomplement)
    x = x[::-1]

    #Setting up the loop variables
    position = 0
    position_reverse = 0
    number_of_ok = 0
    number_of_ok_reverse = 0
    z = 0
    q = 0

    #Go trough the list of codons with the 5'->3' codons
    while z < len(l):

        #If its a complete match and all the amino acids are coded in the correct sequence print it.
        if number_of_ok == len(protein):
            number_of_ok = 0
            counter += 1
            break

        #If the codon is found in the list and the amino acid name matches with the protein variable
        elif l[z][0:3] == codon[position: position + 3] and l[z][4] == protein[number_of_ok]:
            position += 3
            number_of_ok += 1
            z = 0
        else:
            z +=1

    #Go trough the codon list with the complementer codons.
    while q < len(l):

        #If its a complete match and all the amino acids are coded in the correct sequence print it.
        if number_of_ok_reverse == len(protein):
            number_of_ok_reverse = 0
            counter += 1
            break
        #If the codon is found in the list and the amino acid name matches with the protein variable
        elif l[q][0:3] == x[position_reverse: position_reverse + 3] and l[q][4] == protein[number_of_ok_reverse]:
            position_reverse +=3
            number_of_ok_reverse +=1
            q = 0
        else:
            q += 1

print counter
