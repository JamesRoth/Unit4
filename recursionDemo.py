#James Roth
#3/29/18
#recursionDemo.py - recursive version of countdown - a function that calls itself

def countdown(n):
    if n==0: #called the "base case"
        print("BOOM!")
    else: 
        print(n)
        n-=1
        countdown(n)

countdown(1000)
