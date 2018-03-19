#James Roth
#3/19/18
#returnDemo.py - how to use return

from random import randint

def randEven(low,high):
    int=randint(low,high)
    while int%2!=0:
        int=randint(low,high)
    print(n)

randEven(2,20)
