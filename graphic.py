import tkinter
import globalVar
import gate
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

def tileOffsets():
    # Find the total height and width of the map
    mapGraphicWidth=(globalVar.width-1)*globalVar.tileWidth*3/4
    mapGraphicHeight=(globalVar.length-1)*globalVar.tileHeight+(globalVar.width-1)*globalVar.tileHeight/2

    # Use the total height and width of the map to compute offset values that will center the map in the screen
    interface.update()
    tileOffsetX=(interface.winfo_width()-mapGraphicWidth)/2
    tileOffsetY=(interface.winfo_height()-mapGraphicHeight)/2

    return (tileOffsetX,tileOffsetY)

def getTilePosition(x,y):
    tileOffsetX,tileOffsetY=tileOffsets()

    tileX=tileOffsetX+x*globalVar.tileWidth*3/4
    tileY=tileOffsetY+y*globalVar.tileHeight+x*globalVar.tileHeight/2

    return (tileX,tileY)

def getTileFromPixel(x,y):
    tileOffsetX,tileOffsetY=tileOffsets()

    tileX=(x-tileOffsetX)/(globalVar.tileWidth*3/4)
    tileY=(y-(tileOffsetY+tileX*globalVar.tileHeight/2))/globalVar.tileHeight

    return (tileX,tileY)

def roundTile(x,y):
    z=-(x+y)

    roundedX=round(x)
    roundedY=round(y)
    roundedZ=round(z)

    xDiff=abs(x-roundedX)
    yDiff=abs(y-roundedY)
    zDiff=abs(z-roundedZ)

    if xDiff>yDiff and xDiff>zDiff:
        roundedX=-(roundedY+roundedZ)
    elif yDiff>zDiff:
        roundedY=-(roundedX+roundedZ)

    return (roundedX,roundedY)


circleOffsets={}
circleOffsets[globalVar.N]=(0,-108)
circleOffsets[globalVar.NE]=(92,-58)
circleOffsets[globalVar.SE]=(92,24)
circleOffsets[globalVar.S]=(0,75)
circleOffsets[globalVar.SW]=(-92,24)
circleOffsets[globalVar.NW]=(-92,-58)

def inputCircle(x,y,direction):
    centerX,centerY=getTilePosition(x,y)
    centerY-=globalVar.gateExtraHeight/2

    offset=circleOffsets[direction]
    centerX+=offset[0]
    centerY+=offset[1]

    return interface.create_oval(centerX-4,centerY-4,centerX+4,centerY+4,fill='#ff0000',outline='#ff0000')

def outputCircle(x,y,direction):
    centerX,centerY=getTilePosition(x,y)
    centerY-=globalVar.gateExtraHeight/2

    offset=circleOffsets[direction]
    centerX+=offset[0]
    centerY+=offset[1]

    return interface.create_oval(centerX-4,centerY-4,centerX+4,centerY+4,fill='#00ff00',outline='#00ff00')

tileImg=ImageTk.PhotoImage(Image.open('assets/images/empty.png'))

gateImg=ImageTk.PhotoImage(Image.open('assets/images/gatePlatform.png'))

inputImages={}
inputImages[globalVar.N]=ImageTk.PhotoImage(Image.open('assets/images/InputUnlit/Input_N.png'))
inputImages[globalVar.NE]=ImageTk.PhotoImage(Image.open('assets/images/InputUnlit/Input_NE.png'))
inputImages[globalVar.SE]=ImageTk.PhotoImage(Image.open('assets/images/InputUnlit/Input_SE.png'))
inputImages[globalVar.S]=ImageTk.PhotoImage(Image.open('assets/images/InputUnlit/Input_S.png'))
inputImages[globalVar.SW]=ImageTk.PhotoImage(Image.open('assets/images/InputUnlit/Input_SW.png'))
inputImages[globalVar.NW]=ImageTk.PhotoImage(Image.open('assets/images/InputUnlit/Input_NW.png'))

unlitInputs={}
unlitOutputs={}
bindings={}

unlitInputs[gate.multiply]=[ImageTk.PhotoImage(Image.open('assets/images/Gates/And/Unlit/Input'+str(i)+'.png')) for i in [1,2]]
unlitOutputs[gate.multiply]=[ImageTk.PhotoImage(Image.open('assets/images/Gates/And/Unlit/Output1.png'))]
bindings[gate.multiply]=ImageTk.PhotoImage(Image.open('assets/images/Gates/And/Binding.png'))