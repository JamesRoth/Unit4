#James Roth
#3/29/18
#stringInteresct.py - common letter from 2 strings

def stringInt(a,b):
    ans=""
    for ch in a:
        if ch in b:
            ans=ans+str(ch)
