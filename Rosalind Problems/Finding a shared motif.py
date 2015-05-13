#Beolvasni a filet
f = open('sample.txt', 'r').readlines()  # Megnyitja a filet

# Szevenciankent beolvas
l = []
s = ""
for i in range (len(f)):
    if i != 0:
        if f[i][0] == ">":
            l.append(s)
            s = ""
        else:
            s += f[i]
            if i == len(f)-1:
                l.append(s)

# Kiszedi a newlinet
l = [i.replace('\n', '') for i in l]

# Legrovidebb sor
def shortest_seq(l):
    counter = 0
    short_index = 0
    for i in range (len(l)):
        if counter == 0:
            counter += len (l[i])
        if len (l[i]) < counter:
            counter = len (l[i])
            short_index = i
print shortest_seq(l)
# Search motif
def search_motif(seq):
    counter = 1
    for i in range (1,len (l)):
        if seq in l[i]:
            counter += 1
        else:
            return False
    if counter == len(l):
        return True

#Vegigloopolni a legrovidebb soron
k = 2
i = 0
biggest_size = 1
biggest = ""
while i < len (l[0])-1:

    seq = l[0][i:i+k]
    if search_motif (seq) == True:
        if len(seq) >= biggest_size:
            biggest = l[0][i:i+k]
            biggest_size = len(seq)
            print biggest
            k += 1
        else:
            k += 1
    else:
        i +=1
        k = 2


print biggest

#a kapott szekvenciat megkeresi az osszes szekvenciaban
#ha barhol is false akkor return 0
