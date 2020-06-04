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

    pressedGateDirection=None
    pressedGateX=None
    pressedGateY=None

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

def mouseMoveEvent(event):
    global pressedGateDirection
    global pressedGateX
    global pressedGateY

    if pressedGateDirection!=None:
        x=event.x
        y=event.y

        tileX,tileY=graphic.getTileFromPixel(x,y)

        roundedX,roundedY=graphic.roundTile(tileX,tileY)

        tileCenterX,tileCenterY=graphic.getTilePosition(roundedX,roundedY)
        diffX=x-tileCenterX
        diffY=y-tileCenterY
        angle=math.atan2(diffY,diffX)+math.pi
        angleIndex=min(5,math.floor(3*angle/math.pi))
        currentGateDirection=[globalVar.NW,globalVar.N,globalVar.NE,globalVar.SE,globalVar.S,globalVar.SW][angleIndex]

        if currentGateDirection!=pressedGateDirection:
            changed=False
            for i in range(6):
                direction=globalVar.gateMap[pressedGateX][pressedGateY].inputMap[i]
                if direction==pressedGateDirection:
                    if currentGateDirection not in globalVar.gateMap[pressedGateX][pressedGateY].inputMap and currentGateDirection not in globalVar.gateMap[pressedGateX][pressedGateY].outputMap:
                        globalVar.gateMap[pressedGateX][pressedGateY].inputMap[i]=currentGateDirection
                        changed=True
                    break
            for i in range(6):
                direction=globalVar.gateMap[pressedGateX][pressedGateY].outputMap[i]
                if direction==pressedGateDirection:
                    if currentGateDirection not in globalVar.gateMap[pressedGateX][pressedGateY].inputMap and currentGateDirection not in globalVar.gateMap[pressedGateX][pressedGateY].outputMap:
                        globalVar.gateMap[pressedGateX][pressedGateY].outputMap[i]=currentGateDirection
                        changed=True
                    break
            if changed:
                pressedGateDirection=currentGateDirection
    globalVar.mapDisplay.updateGateGraphics()

def createNewGate(x,y):
    map.mapHandler.editTile(x,y,gate.multiply)
    globalVar.gateMap[x][y].setInput(0,globalVar.SW)
    globalVar.gateMap[x][y].setInput(1,globalVar.SE)
    globalVar.gateMap[x][y].setOutput(1,globalVar.N)
    globalVar.mapDisplay.updateGateGraphics()

graphic.interface.bind("<Button-1>",mousePressEvent)
graphic.interface.bind("<B1-Motion>",mouseMoveEvent)