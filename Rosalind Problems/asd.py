__author__ = 'Peter'
# String
s = "When I find myself in times of trouble Mother Mary comes to me Speaking words of wisdom let it be And in my hour of darkness she is standing right in front of me Speaking words of wisdom let it be Let it be let it be let it be let it be Whisper words of wisdom let it be And when the broken hearted people living in the world agree There will be an answer let it be For though they may be parted there is still a chance that they will see There will be an answer let it be Let it be let it be let it be let it be There will be an answer let it be Let it be let it be let it be let it be Whisper words of wisdom let it be Let it be let it be let it be let it be Whisper words of wisdom let it be And when the night is cloudy there is still a light that shines on me Shine until tomorrow let it be I wake up to the sound of music Mother Mary comes to me Speaking words of wisdom let it be Let it be let it be let it be yeah let it be There will be an answer let it be Let it be let it be let it be yeah let it be Whisper words of wisdom let it be"
# Variable declare Where we are in the list
where = 0
#List that i put the items from the string
l = []
#Dictionary
book = {}
how_many = 1
# Split string to list called l
for word in s.split(' '):
    l.append(word)
# Ismételje meg a lista hosszúságával megegyező számban
for i in range(len(l)):
   #Ha a szó már megvan a dictionaryben akkor növelje egyel az értékét
    if l[i] in book:
        book [l[i]] += 1
   #Ha nincs adja hozzá egyes értékkel
    else:
        book [l[i]] = 1

#print
for key, value in book.items():
    print key
    print value
