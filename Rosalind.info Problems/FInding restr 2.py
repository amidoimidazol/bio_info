"""
author: Peter Forgacs
use: Egy txt filebol beolvas egy szekvenciat es megkeresi benne az oszes 4-12 hosszu palindrom szekvenciat es ezeket pozicioval es hosszal kiprinteli
"""
# 3 eldonti hogy megfeleloek e a karakterek OK
def isitcool(x , y):
    if x == "A" and y == "T":
        return True
    elif x=="G" and y == "C":
        return True
    elif x=="C" and y == "G":
        return True
    elif x=="T" and y == "A":
        return True
    else:
        return False

# 2 bekuldi a karaktereket az isitcoolba(3)
def send_to_cool(volt,norm,rev):
    counter = 0
    for x in range(volt):
        var = isitcool (norm[x],rev[x])
        if var is True:
            counter += 1
            if counter == volt:
                q =str (i+1)
                print q,
                print volt
                return 1
        else:
            return 1

# 1 kiszedi a szavakat es bekuldi a send to coolba(2)
def normrev (y,i,volt,x,how_many):
    while x < how_many:
        # Ezzel van gond
        q = i + volt
        norm = y[i:q]
        rev = norm [::-1]
        x += send_to_cool (volt,norm,rev)
        volt +=2





# File beolvasasa es megnyitasa
f = open('reverse.txt', 'r').readlines()[1:]  # Megnyitja a filet
y = str(f)
y = y.translate(None, "\\n" "," "'" " " "[" "]")



l = []
i = 0
# Vegigloopol a beolvasott fileon
for i in range (len (y)):
        volt = 4
        x = 0
        if (len(y)-i) >= 12:
            how_many = 5
            normrev (y,i,volt,x,how_many)
        if (len(y)-i) < 12 and (len(y)-i) >= 10:
            how_many =4
            normrev (y,i,volt,x,how_many)
        elif (len(y)-i) < 10 and (len(y)-i) >= 8:
            how_many = 3
            normrev (y,i,volt,x,how_many)
        elif 6 <= (len(y)-i) and (len(y)-i) < 8:
            how_many = 2
            normrev (y,i,volt,x,how_many)
        elif 4<= (len(y)-i) < 6:
            how_many = 1
            normrev (y,i,volt,x,how_many)