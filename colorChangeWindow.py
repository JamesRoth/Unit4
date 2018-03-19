#James Roth
#3/19/18
#colorChangeWindow.py - function that changes a window's color

from random import randint
from ggame import *

outline=LineStyle(0xffffff,1)

def mouseClick(event):
    int=randint(1,6)
    if int==1:
        color=Color(0x00ff00,1)
    elif int==2:
        color=Color(0xff0000,1)
    elif int==3:
        color=Color(0x0000ff,1)
    elif int==4:
        color=Color(0x00ffff,1)
    elif int==5:
        color=Color(0xff00ff,1)
    else:
        color=Color(0xffffff,1)

rectangle=RectangleAsset(1000,2000,outline,color)

Sprite(rectangle)

App().listenMouseEvent("click", mouseClick)
App.run()
