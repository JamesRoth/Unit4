#James Roth
#3/19/18
#returnDemo.py - how to use return

from random import randint

def randEven(low,high):
    int=randint(low,high)
    while int%2!=0:
        int=randint(low,high)
    return(int)

print("Your even numbers are:", randEven(0,100), randEven(0,100), randEven(0,100))
num4=randEven(1000,2000)
if num4>500:
    print(num4)