#James Roth
#3/22/18
#monkeyBanana.py - a game about monkeys and bananas - the "best game ever"

from ggame import *
from random import randint

#constants
ROWS = 28
COLUMNS = 52
CELL_SIZE = 20

#functions
def moveRight(event):
    if monkey.x<(COLUMNS-2)*CELL_SIZE:
        monkey.x+=CELL_SIZE
        if monkey.x==banana.x and monkey.y==banana.y:
            moveBanana()
            data{"score"}+=10
            print(data{"score"})

def moveLeft(event):
    if monkey.x>0:
        monkey.x-=CELL_SIZE
        if monkey.x==banana.x and monkey.y==banana.y:
            moveBanana()
            data{"score"}+=10
            print(data{"score"})

def moveUp(event):
    if monkey.y>0:
        monkey.y-=CELL_SIZE
        if monkey.x==banana.x and monkey.y==banana.y:
            moveBanana()
            data{"score"}+=10
            print(data{"score"})

def moveDown(event):
    if monkey.y<(ROWS-2)*CELL_SIZE:
        monkey.y+=CELL_SIZE
        if monkey.x==banana.x and monkey.y==banana.y:
            moveBanana()
            data{"score"}+=10
            print(data{"score"})
    
def moveBanana():
    banana.x=randint(1,COLUMNS-2)*CELL_SIZE
    banana.y=randint(1,ROWS-2)*CELL_SIZE

if __name__ == "__main__":
    
    #hold variables in a dictionary
    data={}
    data{"score"} = 0
    
    #colors
    green=Color(0x006600,1)
    brown=Color(0x8b4513,1)
    yellow=Color(0xffff00,1)
    
    jungleBox=RectangleAsset(CELL_SIZE*COLUMNS,CELL_SIZE*ROWS,LineStyle(1,green),green)
    monkeyBox=RectangleAsset(CELL_SIZE,CELL_SIZE,LineStyle(1,brown),brown)
    bananaBox=RectangleAsset(CELL_SIZE,CELL_SIZE,LineStyle(1,yellow),yellow)
    
    Sprite(jungleBox)
    monkey=Sprite(monkeyBox)
    banana=Sprite(bananaBox,(CELL_SIZE*COLUMNS/2,CELL_SIZE*ROWS/2))
    
    App().listenKeyEvent("keydown","right arrow",moveRight)
    App().listenKeyEvent("keydown","left arrow",moveLeft)
    App().listenKeyEvent("keydown","up arrow",moveUp)
    App().listenKeyEvent("keydown","down arrow",moveDown)
    App().run()
