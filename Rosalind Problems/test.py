peptide = 'PETI'

new_str = list(peptide)


new_str.insert(0, new_str[len(new_str)-1])
del(new_str[len(new_str)-1])
final = ''.join(new_str)
print final