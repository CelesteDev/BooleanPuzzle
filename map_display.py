import graphic
import globalVar

class MapDisplay:

    def __init__(self, interface):
        self.interface=interface
        self.tileSprites=[]
        self.gateSprites=[]

        for i in range(globalVar.width):
            tileColumn=[]
            for i2 in range(globalVar.length):
                tileX,tileY=graphic.getTilePosition(i,i2)
                newTile=interface.create_image(tileX, tileY, image=graphic.tileImg)
                tileColumn.append(newTile)
            self.tileSprites.append(tileColumn)

        self.gateSprites=[[None for i2 in range(globalVar.length)] for i in range(globalVar.width)]

    def loadGateGraphics(self):
        for i in range(globalVar.width):
            for i2 in range(globalVar.length):
                if globalVar.gateMap[i][i2]!=None:
                    tileX,tileY=graphic.getTilePosition(i,i2)

                    self.gateSprites[i][i2]=self.interface.create_image(tileX, tileY, image=graphic.gateImage(globalVar.gateMap[i][i2]))

                    for inputDirection in globalVar.gateMap[i][i2].inputMap:
                        if inputDirection!=None:
                            edgeX,edgeY=graphic.getEdgePosition(inputDirection)
                            self.interface.create_image(tileX+edgeX*0.8,tileY+edgeY*0.8,image=graphic.inputImages[inputDirection])

