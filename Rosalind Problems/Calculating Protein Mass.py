'''

Author: Peter Chip (furamail001@gmail.com)

Date: 2015 04 05

Given: A protein string P of length at most 1000 aa.

Return: The total weight of P. Consult the monoisotopic mass table.

                                A   71.03711
                                C   103.00919
                                D   115.02694
                                E   129.04259
                                F   147.06841
                                G   57.02146
                                H   137.05891
                                I   113.08406
                                K   128.09496
                                L   113.08406
                                M   131.04049
                                N   114.04293
                                P   97.05276
                                Q   128.05858
                                R   156.10111
                                S   87.03203
                                T   101.04768
                                V   99.06841
                                W   186.07931
                                Y   163.06333

Theory:
'''

# TODO Make the file readin and formatting nicer, with read in functions
f = open('calculating_protein_mass.txt')
text = f.readlines()

# Removing Whitespace
def lose_the_whitespace(text):
        return text.replace(" ","")

# Removing Newlines
def lose_the_newline(text):
        return text.replace("\n","")

# Calling the clean functions
L = []
for line in text:
    L.append(lose_the_newline(lose_the_whitespace(line)))
print(L)

# Adding the list element to a dictionary
D = {}
for i in L:
    D[i[0:1]] = float(i[1:len(i)])
print(D)

protein_string = "ITHTVEWGALLAVLKGYCEQTTSWWVGTWVVPNVGYDFMQRMNIPMWINNLPIPQCQVNGYLFDWPMFFTGDYDQVTLFTGHRGHAEREDMYWKTQEGEIQARSEDVNSGMQRACLLETYNEAWIMTGITGPLAFPIYRHIGKFTLSVCSNAAGLLEKWDHSLWRTIAQHHVMCHCLGCEVWMCCSKKDKHGHASNRLTEPMQADHFNPCDKFQCRELILMPGNVGDNVMWMYGYNNTINKLPMKIKRACDHHAYNRLRRQFNSAILWVPGVQNKDLVNDHQGGGFFVLIMAHKVRPWWRAETWSEDFLLRKVLDRNQTIHARWDYIFLTKMHWWCFEKIALLLGAIYFTYDTAYRPCKNRHHVQGPRPDRGYDPMGYSCYSVLNIEKVYCRRWVCWTNTYKYRKIFWWKQSNVYPECSYMNLEYIHSWDCFTANMVYTCGGFGQWWRYANDNLCPMIMVQKSHIGFFYGNDATLCNLQALLRPMWTRNIPCQTTVSWLESDYIRWVKKAYSAQDVDFGHGPMGYMNENHPCDDSPWHMIQINHLGHRMICCIANGKNCYKEHKTRLQKMWHITMKCYQALMMSTADGTGQDAGPKVPRWTSENMWRIDFGEIFWDETTRHDGCRFQELERPMSWMNQCTMDMTYNFSQVWMGMDVMGQRTPTILIRYFLHSNNLRPQNFEWMKGCRVDHCICFMCHTDSWMWMFMIMWTYHMWMAPKACDIHTIYRVLEFCLYGNFMAHANQWMRATSKQGYQMPSMVVWRTTDNGFHDFPPPMNTKMRWYSYSKMMGIDPFVNNCCNNNEMVRRVMAPKQGWHWEQCMLAEVFELTYMARYKTMIGFMKRLYEGVLCKTVPARLYGYDNQLGFQEACKQPFEICELTKVEFVTMMLDQCLQCCIAKQNCAPWLCSLMNHQDTGMRQD"

# Adding the value of the character
value = 0
for i in protein_string:
    value += D[i]
print(value)