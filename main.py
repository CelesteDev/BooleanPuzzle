import graphic
import input_handler
import map_display
import tkinter
import map
import gate
import globalVar

def loop():
    ##Function runned every Frames

    graphic.interface.after(30,loop) #function calling itself after 30ms

loop()



map.mapHandler.create(3,3)
'''map.mapHandler.editTile(0,2,gate.on)
globalVar.gateMap[0][2].setOutput(0,globalVar.NE)

map.mapHandler.editTile(2,1,gate.debugger)
globalVar.gateMap[2][1].setInput(0,globalVar.SW)

map.mapHandler.editTile(1,0,gate.debugger)
globalVar.gateMap[1][0].setInput(0,globalVar.S)

map.mapHandler.editTile(1,1,gate.wire)
globalVar.gateMap[1][1].togglePort(globalVar.SW)
globalVar.gateMap[1][1].togglePort(globalVar.N)
globalVar.gateMap[1][1].togglePort(globalVar.NE)'''

map.mapHandler.editTile(1,1,gate.multiply)
globalVar.gateMap[1][1].setInput(0,globalVar.SW)
globalVar.gateMap[1][1].setInput(1,globalVar.SE)
globalVar.gateMap[1][1].setOutput(1,globalVar.N)

map.mapHandler.editTile(2,1,gate.multiply)
globalVar.gateMap[2][1].setInput(0,globalVar.SW)
globalVar.gateMap[2][1].setInput(1,globalVar.S)
globalVar.gateMap[2][1].setOutput(1,globalVar.NW)

map.mapHandler.stepSim()

mapDisplay=map_display.MapDisplay(graphic.interface)
mapDisplay.updateGateGraphics()

globalVar.mapDisplay=mapDisplay

graphic.interface.mainloop() #initialising the window
