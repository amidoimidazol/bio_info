"""
Author: Peter Forgacs

Date: 2014.03.27

Description: Makes a theoretical spectrum of the given peptide sequence. Gets all the possible subpeptides and lists their masses.

Question:

Development: Missing NL if the turnaround is 2. The problem is with the variables starting with 1. If the turnaround is 2 x
            evaluates to false. If x starts at 0 it evaluates to true NL shows up but additional sequences show up because ?

"""
# Set up variables for the peptide
peptide = 'LEQN'
n = len(peptide)
subpeptides = []
new_str = list(peptide)

# Read in amino acid masses
f = open('mass.txt', 'r')
l = f.readlines()
f.close()

# Generate all the possible subpeptides
for i in range(2):
    if i == 0:
        for z in peptide:
            subpeptides.append(z)
    else:
        repeat = 0
        # The number of subpeptides that you cant read out straight from the peptide variable
        turnaround = 2
        # Repeat at every possible length of subpeptide wich length dosent equal 1
        while repeat < n-2:
            # Repeat at a certain length n times starting at 1
            for q in range(1,n+1,):
                if q <= n - turnaround +1:
                    subpeptides.append(peptide[q-1:q+turnaround-1])
                elif q > n - turnaround + 1:
                    for x in range(1,turnaround-1):
                        new_str.insert(0, new_str[len(new_str)-1])
                        del(new_str[len(new_str)-1])
                        final = ''.join(new_str)
                        subpeptides.append(final[0:turnaround])

            new_str = list(peptide)
            turnaround += 1
            repeat += 1
print subpeptides

# Find out the masses of the subpeptides and save it in a new list wich starts with 0 and ends with the total mass
# Print out solution