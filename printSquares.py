#James Roth
#3/26/18
#printSquares - function that prints squares 

def squares(c,r):
    print("+--+--"*(r-1) + "+")
    while c>1: 
        print("|  |  "*(r-1) + "|")
        print("+--+--"*(r-1) + "+")
        c-=1
    print("|  |  " + "|")
    print("+--+--" + "+")
squares(2,4)
