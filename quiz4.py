#James Roth
#4/2/18
#quiz4.py

def count(a):
    for i in range(1, a+1):
        print(i)

def excitedPrint(a):
    a=a.upper()
    print(a+"!!!")

def firstLetter(a):
    for ch in a:
        return ch

def repeats(a,b,c):
    if a==b or b==c or a==c:
        return True
    else:
        return False

print(repeats(10,5,10))