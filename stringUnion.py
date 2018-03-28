#James Roth
#3/28/18
#stringUion.py - joining letters

def stringUnion(w1,w2):
    string=""
    for ch in w1:
        if ch not in string:
            string+=ch
    for ch in w2:
        if ch not in string:
            string+=ch
    return(string)

print(stringUnion("Mississippi", "Pennsylvania"))
