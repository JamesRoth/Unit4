#James Roth
#3/26/18
#printSquares - function that prints squares 

def squares(c,r):
    print("+--+--"*c)
    while r>1: 
        print("|  |  "*c)
        print("+--+--"*c)
        r-=1
    print("|  |"*c)
    print("+--+"*c)
squares(2,4)
