#James Roth
#3/22/18
#monkeyBanana.py - a game about monkeys and bananas - the "best game ever"

from ggame import *

#constants
ROWS = 30
COLUMNS = 52
CELL_SIZE = 20

#functions
def moveRight(event):
    monkey.x+=CELL_SIZE

def moveLeft(event):
    monkey.x-=CELL_SIZE

def moveUp(event):
    monkey.y-=CELL_SIZE

def moveDown(event):
    monkey.y+=CELL_SIZE

if __name__ == "__main__":
    
    #colors
    green=Color(0x006600,1)
    brown=Color(0x8b4513,1)
    yellow=Color(0xffff00,1)
    
    jungleBox=RectangleAsset(CELL_SIZE*COLUMNS,CELL_SIZE*ROWS,LineStyle(1,green),green)
    monkeyBox=RectangleAsset(CELL_SIZE,CELL_SIZE,LineStyle(1,brown),brown)
    bananaBox=RectangleAsset(CELL_SIZE,CELL_SIZE,LineStyle(1,yellow),yellow)
    
    Sprite(jungleBox)
    monkey=Sprite(monkeyBox)
    banana=Sprite(bananaBox)
    
    App().listenKeyEvent("keydown","right arrow",moveRight)
    App().listenKeyEvent("keydown","left arrow",moveLeft)
    App().listenKeyEvent("keydown","up arrow",moveUp)
    App().listenKeyEvent("keydown","down arrow",moveDown)
    App().run()
