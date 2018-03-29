#James Roth
#3/29/18
#stringInteresct.py - common letter from 2 strings

def stringInt(a,b):
    a=a.lower()
    b=b.lower()
    ans=""
    for ch in a:
        if ch in b:
            ans=ans+str(ch)
    return ans

stringInt("James", "Andrew")