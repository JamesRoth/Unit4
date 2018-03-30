#James Roth
#3/29/18
#triangle.py - verticies to area of a triangle

def distance(x1, y1, x2, y2):
    return(((y1-y2)**2 + (x1-x2)**2)**(1/2))

def area(x1, y2, x2, y2, x3, y3):
    side1=distance(x1, y1, x2, y2)
    side2=distance(x2, y2, x3, y3)
    side3=distance(x3, y3, x1, y1)
    
