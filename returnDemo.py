#James Roth
#3/19/18
#returnDemo.py - how to use return

from random import randint

def randEven(low,high):
    int=randint(low,high)
    if int%2==0:
        print(int)
    else:
        randEven(low,high)

randEven(2,20)
