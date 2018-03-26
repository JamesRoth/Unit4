#James Roth
#3/26/18
#printSquares - function that prints squares 

"""
def squares(r,c):
    print("+--+--"*(r-1) + "+")
    while c>1: 
        print("|  |  "*(r-1) + "|")
        print("+--+--"*(r-1) + "+")
        c-=1
    print("|  |  " + "|")
    print("+--+--" + "+")
squares(2,4)
squares(4,2)
"""

def squares(r,c):
        print("+--"*c + "+")
        print("|  "*c + "|")

squares(2,4)