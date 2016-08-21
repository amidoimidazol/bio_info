__author__ = 'Peter'
# String
s = "Peter Peter peter peter"
# Variable declare Where we are in the list
where = 0
#List that i put the items from the string
l = []
#Dictionary
book = {}
how_many = 1
# Split string to list
for word in s.split(' '):
    l.append(word)
for l[where] in l:
    if 'l[where]' in book:
        book [l[where]] += 1
        l.remove(l[where])
        where += 1
        print "book"
        print book
        print "list"
        print l

    else:
        book [l[where]] = how_many
        l.remove(l[where])
        where += 1
        print "book"
        print book
        print "list"
        print l
        print "where %s"% where

"""
#Vegigmenni  a listen egy loopban
while where <= len(l):
    #Szerepel-e a szo tobbszor
    x = l[where]
    #Variable declare how many words are there
    how_many = 0
    where += 1
    if x in l:
        how_many += 1
        book[x] = how_many
        l.remove(x)
"""


print "final%s" % book
print "final%s"%  list
