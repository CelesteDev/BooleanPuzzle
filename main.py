import graphic
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
map.mapHandler.editTile(0,2,gate.on)
globalVar.gateMap[0][2].setOutput(0,globalVar.NE)

map.mapHandler.editTile(2,1,gate.debugger)
globalVar.gateMap[2][1].setInput(0,globalVar.SW)

map.mapHandler.editTile(1,0,gate.debugger)
globalVar.gateMap[1][0].setInput(0,globalVar.S)

map.mapHandler.editTile(1,1,gate.wire)
globalVar.gateMap[1][1].togglePort(globalVar.SW)
globalVar.gateMap[1][1].togglePort(globalVar.N)
globalVar.gateMap[1][1].togglePort(globalVar.NE)

map.mapHandler.stepSim()

print(globalVar.valueMap)

print("\ninputs:")
print(globalVar.gateMap[0][2].inputMap)
print(globalVar.gateMap[2][1].inputMap)
print(globalVar.gateMap[1][0].inputMap)
print(globalVar.gateMap[1][1].inputMap)

print("\noutputs:")
print(globalVar.gateMap[0][2].outputMap)
print(globalVar.gateMap[2][1].outputMap)
print(globalVar.gateMap[1][0].outputMap)
print(globalVar.gateMap[1][1].outputMap)

mapDisplay=map_display.MapDisplay(graphic.interface)
mapDisplay.loadGateGraphics()

graphic.interface.mainloop() #initialising the window
