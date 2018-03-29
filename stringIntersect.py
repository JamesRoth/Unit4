#James Roth
#3/29/18
#stringInteresct.py - common letters from 2 strings

def stringInt(a,b):
    a=a.lower()
    b=b.lower()
    ans=""
    for ch in a:
        if ch in b and ch not in ans:
            ans=ans+ch
    return ans

print(stringInt("James", "Andrew"))