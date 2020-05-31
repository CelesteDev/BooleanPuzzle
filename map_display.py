import graphic
import globalVar

tileWidth=160
tileHeight=120

class MapDisplay:

    def __init__(self, interface):
        self.interface=interface
        self.tileSprites=[]
        self.gateSprites=[]

        for i in range(globalVar.width):
            tileColumn=[]
            for i2 in range(globalVar.length):
                tileX,tileY=self.getTilePosition(i,i2)
                newTile=interface.create_image(tileX, tileY, image=graphic.tileImg)
                tileColumn.append(newTile)
            self.tileSprites.append(tileColumn)

        self.gateSprites=[[None for i2 in range(globalVar.length)] for i in range(globalVar.width)]

    def loadGateGraphics(self):
        for i in range(globalVar.width):
            for i2 in range(globalVar.length):
                if globalVar.gateMap[i][i2]!=None:
                    tileX,tileY=self.getTilePosition(i,i2)
                    self.gateSprites[i][i2]=self.interface.create_image(tileX, tileY, image=graphic.gateImage(globalVar.gateMap[i][i2]))

    def getTilePosition(self,x,y):
        # Find the total height and width of the map
        mapGraphicWidth=(globalVar.width-1)*tileWidth*3/4
        mapGraphicHeight=(globalVar.length-1)*tileHeight+(globalVar.width-1)*tileHeight/2

        # Use the total height and width of the map to compute offset values that will center the map in the screen
        self.interface.update()
        tileOffsetX=(self.interface.winfo_width()-mapGraphicWidth)/2
        tileOffsetY=(self.interface.winfo_height()-mapGraphicHeight)/2

        tileX=tileOffsetX+x*tileWidth*3/4
        tileY=tileOffsetY+y*tileHeight+x*tileHeight/2

        return (tileX,tileY)