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


map.mapHandler.create(4,3)
map.mapHandler.editTile(0,2,gate.off)
globalVar.gateMap[0][2].setOutput(0,globalVar.NE)
map.mapHandler.editTile(1,1,gate.debugger)
globalVar.gateMap[1][1].setInput(0,globalVar.SW)
map.mapHandler.editTile(2,2,gate.on)
map.mapHandler.stepSim()

mapDisplay=map_display.MapDisplay(graphic.interface)
mapDisplay.loadGateGraphics()

graphic.interface.mainloop() #initialising the window
