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

print(firstLetter("James"))