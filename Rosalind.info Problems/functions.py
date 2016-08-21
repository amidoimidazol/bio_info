__author__ = 'Peter Chip'

def lose_the_whitespace(text):
    L = []
    for i in text:
        L.append(i.replace(" ",""))
    return L

def lose_the_newline(text):
    L = []
    for i in text:
        L.append(i.replace("\n",""))
    return L