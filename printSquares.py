#James Roth
#3/26/18
#printSquares - function that prints squares 

def squares(r,c):
    while r>0:
        print("+--"*c + "+")
        print("|  "*c + "|")
        r-=1
    print("+--"*c + "+")

squares(2,4)
squares(4,2)