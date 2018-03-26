#James Roth
#3/26/18
#printSquares - function that prints squares 

def squares(r,c):
    print("+--+--"*(c-1) + "+")
    while r>1: 
        print("|  |  "*(c-1) + "|")
        print("+--+--"*(c-1) + "+")
        r-=1
    print("|  |  " + "|")
    print("+--+--" + "+")
squares(2,4)
