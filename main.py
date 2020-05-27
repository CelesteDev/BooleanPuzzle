import graphic

def loop(frame):
    ##Function runned every Frames

    graphic.interface.after(30,loop) #function calling itself after 30ms

loop()

graphic.interface.mainloop() #initialising the window

