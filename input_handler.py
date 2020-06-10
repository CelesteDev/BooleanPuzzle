import tkinter
import globalVar
import graphic
import gate
import map
import math

pressedGateX=None
pressedGateY=None
pressedGateDirection=None

selectedGateIndex=0

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

    tileCenterX,tileCenterY=graphic.getTilePosition(roundedX,roundedY)
    diffX=x-tileCenterX
    diffY=y-tileCenterY
    angle=math.atan2(diffY,diffX)+math.pi
    angleIndex=math.floor(3*angle/math.pi)
    pressedDirection=[globalVar.NW,globalVar.N,globalVar.NE,globalVar.SE,globalVar.S,globalVar.SW][angleIndex]

    if selectedGateIndex==-1:
        if globalVar.gateMap[roundedX][roundedY]==None:
            createWire(roundedX,roundedY)
        addWireDirection(roundedX,roundedY,pressedDirection)
    else:
        if globalVar.gateMap[roundedX][roundedY]==None:
            createNewGate(roundedX,roundedY)
        else:
            pressedGateDirection=pressedDirection
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

def rightMousePressEvent(event):
    global selectedGateIndex
    selectedGateIndex=-1
    globalVar.mapDisplay.moveSelectedGateIcon(selectedGateIndex)

def mousewheelEvent(event):
    global selectedGateIndex

    if selectedGateIndex==-1:
        selectedGateIndex=0
    else:
        if(event.delta>0):
            selectedGateIndex=selectedGateIndex-1
        else:
            selectedGateIndex=selectedGateIndex+1
    selectedGateIndex=selectedGateIndex%len(globalVar.mapDisplay.availableGates)
    globalVar.mapDisplay.moveSelectedGateIcon(selectedGateIndex)

def createNewGate(x,y):
    gateType=globalVar.mapDisplay.availableGates[selectedGateIndex]
    map.mapHandler.editTile(x,y,gateType)   
    globalVar.gateMap[x][y].setInput(0,globalVar.SW)
    globalVar.gateMap[x][y].setInput(1,globalVar.SE)
    globalVar.gateMap[x][y].setOutput(1,globalVar.N)
    globalVar.mapDisplay.updateGateGraphics()

def createWire(x,y):
    gateType=globalVar.mapDisplay.availableGates[selectedGateIndex]
    map.mapHandler.editTile(x,y,gate.wire)
    globalVar.mapDisplay.updateGateGraphics()

def addWireDirection(x,y,direction):
    globalVar.gateMap[x][y].togglePort(direction)
    globalVar.mapDisplay.updateGateGraphics()

graphic.interface.bind("<Button-1>",mousePressEvent)
graphic.interface.bind("<Button-3>",rightMousePressEvent)
graphic.interface.bind("<B1-Motion>",mouseMoveEvent)
graphic.interface.bind("<MouseWheel>",mousewheelEvent)