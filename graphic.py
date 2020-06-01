import tkinter
import globalVar
from PIL import Image, ImageTk
import math

    #Window Initialisation

#Defining Canvas Settings
windowHeight=1000
windowWidth=1720
color="#ffeeff" #hex for pink
window=tkinter.Tk()
interface=tkinter.Canvas(window,height=windowHeight,width=windowWidth,bg=color,highlightthickness=0)
interface.pack(fill=tkinter.BOTH) #Removing Borderss
window.attributes("-fullscreen",True)

def getTilePosition(x,y):
    # Find the total height and width of the map
    mapGraphicWidth=(globalVar.width-1)*globalVar.tileWidth*3/4
    mapGraphicHeight=(globalVar.length-1)*globalVar.tileHeight+(globalVar.width-1)*globalVar.tileHeight/2

    # Use the total height and width of the map to compute offset values that will center the map in the screen
    interface.update()
    tileOffsetX=(interface.winfo_width()-mapGraphicWidth)/2
    tileOffsetY=(interface.winfo_height()-mapGraphicHeight)/2

    tileX=tileOffsetX+x*globalVar.tileWidth*3/4
    tileY=tileOffsetY+y*globalVar.tileHeight+x*globalVar.tileHeight/2

    return (tileX,tileY)

def getEdgePosition(direction):
    if direction==globalVar.N:
        return (0,-globalVar.tileHeight/2)
    if direction==globalVar.NE:
        return (globalVar.tileWidth*3/8,-globalVar.tileHeight/4)
    if direction==globalVar.SE:
        return (globalVar.tileWidth*3/8,globalVar.tileHeight/4)
    if direction==globalVar.S:
        return (0,globalVar.tileHeight/2)
    if direction==globalVar.SW:
        return (-globalVar.tileWidth*3/8,globalVar.tileHeight/4)
    if direction==globalVar.NW:
        return (-globalVar.tileWidth*3/8,-globalVar.tileHeight/4)

def getDirectionAngle(direction):
	edgePosition=getEdgePosition(direction)
	radians=math.atan2(edgePosition[1],edgePosition[0])+math.pi
	return 180*radians/math.pi+180

tileImg=ImageTk.PhotoImage(Image.open('assets/images/tile.png'))

gateOff=ImageTk.PhotoImage(Image.open('assets/images/gate_off.png'))
gateOn=ImageTk.PhotoImage(Image.open('assets/images/gate_on.png'))
gateDebugger=ImageTk.PhotoImage(Image.open('assets/images/gate_debugger.png'))
gateWire=ImageTk.PhotoImage(Image.open('assets/images/gate_wire.png'))

inputImages={}
for direction in [globalVar.N,globalVar.NE,globalVar.SE,globalVar.S,globalVar.SW,globalVar.NW]:
	image=Image.open('assets/images/input.png').rotate(getDirectionAngle(direction))
	inputImages[direction]=ImageTk.PhotoImage(image)

def gateImage(gate):
	if gate.__class__.__name__=='off':
		return gateOff
	if gate.__class__.__name__=='on':
		return gateOn
	if gate.__class__.__name__=='debugger':
		return gateDebugger
	if gate.__class__.__name__=='wire':
		return gateWire
