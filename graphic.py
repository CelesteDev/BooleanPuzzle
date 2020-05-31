import tkinter

    #Window Initialisation

#Defining Canvas Settings
windowHeight=1000
windowWidth=1720
color="#ffeeff" #hex for pink
window=tkinter.Tk()
interface=tkinter.Canvas(window,height=windowHeight,width=windowWidth,bg=color,highlightthickness=0)
interface.pack(fill=tkinter.BOTH) #Removing Borderss
window.attributes("-fullscreen",True)

tileImg=tkinter.PhotoImage(file='assets/images/tile.png')

gateOff=tkinter.PhotoImage(file='assets/images/gate_off.png')
gateOn=tkinter.PhotoImage(file='assets/images/gate_on.png')
gateDebugger=tkinter.PhotoImage(file='assets/images/gate_debugger.png')

def gateImage(gate):
	if gate.__class__.__name__=='off':
		return gateOff
	if gate.__class__.__name__=='on':
		return gateOn
	if gate.__class__.__name__=='debugger':
		return gateDebugger