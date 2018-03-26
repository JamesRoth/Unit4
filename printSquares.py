#James Roth
#3/26/18
#printSquares - function that prints squares 

def squares(c,r):
    print("+--+--"*(c-1) + "+")
    while r>1: 
        print("|  |  "*(c-1) + "|")
        print("+--+--"*(c-1) + "+")
        r-=1

squares(2,4)
