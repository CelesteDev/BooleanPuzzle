import tkinter
import globalVar
import graphic
import gate
import map
import math

pressedGateX=None
pressedGateY=None
pressedGateDirection=None

def mousePressEvent(event):
    global pressedGateDirection
    global pressedGateX
    global pressedGateY

    x=event.x
    y=event.y

    tileX,tileY=graphic.getTileFromPixel(x,y)

    roundedX,roundedY=graphic.roundTile(tileX,tileY)

    if(globalVar.gateMap[roundedX][roundedY]==None):
        createNewGate(roundedX,roundedY)
    else:
        tileCenterX,tileCenterY=graphic.getTilePosition(roundedX,roundedY)
        diffX=x-tileCenterX
        diffY=y-tileCenterY
        angle=math.atan2(diffY,diffX)+math.pi
        angleIndex=math.floor(3*angle/math.pi)
        pressedGateDirection=[globalVar.NW,globalVar.N,globalVar.NE,globalVar.SE,globalVar.S,globalVar.SW][angleIndex]
        pressedGateX=roundedX
        pressedGateY=roundedY

def mouseReleaseEvent(event):
    global pressedGateDirection
    global pressedGateX
    global pressedGateY
    
    x=event.x
    y=event.y

    tileX,tileY=graphic.getTileFromPixel(x,y)

    roundedX,roundedY=graphic.roundTile(tileX,tileY)

    if pressedGateDirection!=None:
        tileCenterX,tileCenterY=graphic.getTilePosition(roundedX,roundedY)
        diffX=x-tileCenterX
        diffY=y-tileCenterY
        angle=math.atan2(diffY,diffX)+math.pi
        angleIndex=math.floor(3*angle/math.pi)
        releasedGateDirection=[globalVar.NW,globalVar.N,globalVar.NE,globalVar.SE,globalVar.S,globalVar.SW][angleIndex]
        if releasedGateDirection!=pressedGateDirection:
            for i in range(6):
                direction=globalVar.gateMap[pressedGateX][pressedGateY].inputMap[i]
                if direction==pressedGateDirection:
                    globalVar.gateMap[pressedGateX][pressedGateY].inputMap[i]=releasedGateDirection
                    print("moving input from",direction,"to",releasedGateDirection)
                    break
            for i in range(6):
                direction=globalVar.gateMap[pressedGateX][pressedGateY].outputMap[i]
                if direction==pressedGateDirection:
                    globalVar.gateMap[pressedGateX][pressedGateY].outputMap[i]=releasedGateDirection
                    print("moving output from",direction,"to",releasedGateDirection)
                    break
    pressedGateDirection=None

def createNewGate(x,y):
    map.mapHandler.editTile(x,y,gate.multiply)
    globalVar.gateMap[x][y].setInput(0,globalVar.SW)
    globalVar.gateMap[x][y].setInput(1,globalVar.SE)
    globalVar.gateMap[x][y].setOutput(1,globalVar.N)
    globalVar.mapDisplay.updateGateGraphics()

graphic.interface.bind("<Button-1>",mousePressEvent)
graphic.interface.bind("<ButtonRelease-1>",mouseReleaseEvent)