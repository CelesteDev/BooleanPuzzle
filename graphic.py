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

