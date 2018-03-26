#James Roth
#3/26/18
#printSquares - function that prints squares 

def squares(c,r):
    print("+--+"*c)
    while r>0: 
        print("|  |"*c)
        print("+--+"*c)
    r-=1
squares(2,4)
