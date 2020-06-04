import graphic
import globalVar

class MapDisplay:

    def __init__(self, interface):
        self.interface=interface
        self.tileSprites=[]

        for i in range(globalVar.width):
            tileColumn=[]
            for i2 in range(globalVar.length):
                tileX,tileY=graphic.getTilePosition(i,i2)
                newTile=interface.create_image(tileX, tileY, image=graphic.tileImg)
                tileColumn.append(newTile)
            self.tileSprites.append(tileColumn)

        self.gateBaseSprites=[[None for i2 in range(globalVar.length)] for i in range(globalVar.width)]

        self.inputPortDirections=[[[None for i3 in range(6)] for i2 in range(globalVar.length)] for i in range(globalVar.width)]
        self.inputPortSprites=[[[None for i3 in range(6)] for i2 in range(globalVar.length)] for i in range(globalVar.width)]
        self.inputPortCircles=[[[None for i3 in range(6)] for i2 in range(globalVar.length)] for i in range(globalVar.width)]

        self.outputPortDirections=[[[None for i3 in range(6)] for i2 in range(globalVar.length)] for i in range(globalVar.width)]
        self.outputPortSprites=[[[None for i3 in range(6)] for i2 in range(globalVar.length)] for i in range(globalVar.width)]
        self.outputPortCircles=[[[None for i3 in range(6)] for i2 in range(globalVar.length)] for i in range(globalVar.width)]

        self.gateInputSprites=[[[None for i3 in range(6)] for i2 in range(globalVar.length)] for i in range(globalVar.width)]
        self.gateOutputSprites=[[[None for i3 in range(6)] for i2 in range(globalVar.length)] for i in range(globalVar.width)]
        self.gateBindingSprites=[[None for i2 in range(globalVar.length)] for i in range(globalVar.width)]

    def updateGateGraphics(self):
        for i in range(globalVar.width):
            for i2 in range(globalVar.length):
                if globalVar.gateMap[i][i2]!=None:
                    tileX,tileY=graphic.getTilePosition(i,i2)
                    tileY-=globalVar.gateExtraHeight/2

                    if self.gateBaseSprites[i][i2]==None:
                        self.gateBaseSprites[i][i2]=self.interface.create_image(tileX, tileY, image=graphic.gateImg)

                    for i3 in range(6):
                        inputDirection=globalVar.gateMap[i][i2].inputMap[i3]
                        storedDirection=self.inputPortDirections[i][i2][i3]
                        if inputDirection!=storedDirection:
                            if storedDirection!=None:
                                self.interface.delete(self.inputPortSprites[i][i2][storedDirection])
                                self.interface.delete(self.inputPortCircles[i][i2][storedDirection])
                            if inputDirection!=None:
                                self.inputPortSprites[i][i2][inputDirection]=self.interface.create_image(tileX,tileY,image=graphic.inputImages[inputDirection])
                                self.inputPortCircles[i][i2][inputDirection]=graphic.inputCircle(i,i2,inputDirection)
                            
                            self.inputPortDirections[i][i2][i3]=inputDirection
                    for i3 in range(6):
                        outputDirection=globalVar.gateMap[i][i2].outputMap[i3]
                        storedDirection=self.outputPortDirections[i][i2][i3]
                        if outputDirection!=storedDirection:
                            if storedDirection!=None:
                                self.interface.delete(self.outputPortSprites[i][i2][storedDirection])
                                self.interface.delete(self.outputPortCircles[i][i2][storedDirection])
                            if outputDirection!=None:
                                self.outputPortSprites[i][i2][outputDirection]=self.interface.create_image(tileX,tileY,image=graphic.inputImages[outputDirection])
                                self.outputPortCircles[i][i2][outputDirection]=graphic.outputCircle(i,i2,outputDirection)
                            
                            self.outputPortDirections[i][i2][i3]=outputDirection

                    gateClass=globalVar.gateMap[i][i2].__class__
                    for i3 in range(globalVar.gateMap[i][i2].inputAmount):
                        if self.gateInputSprites[i][i2][i3]==None:
                            self.gateInputSprites[i][i2][i3]=self.interface.create_image(tileX,tileY,image=graphic.unlitInputs[gateClass][i3])
                    for i3 in range(globalVar.gateMap[i][i2].outputAmount):
                        if self.gateOutputSprites[i][i2][i3]==None:
                            self.gateOutputSprites[i][i2][i3]=self.interface.create_image(tileX,tileY,image=graphic.unlitOutputs[gateClass][i3])
                    if self.gateBindingSprites[i][i2]==None:
                        self.gateBindingSprites[i][i2]=self.interface.create_image(tileX,tileY,image=graphic.bindings[gateClass])

        self.layerGateGraphics()

    def layerGateGraphics(self):
        for i in range(globalVar.length):
            for i2 in range(globalVar.width):
                if self.gateBaseSprites[i2][i]!=None:
                    self.interface.tag_raise(self.gateBaseSprites[i2][i])
                    for i3 in range(6):
                        if self.gateInputSprites[i2][i][i3]!=None:
                            self.interface.tag_raise(self.gateInputSprites[i2][i][i3])
                        if self.gateOutputSprites[i2][i][i3]!=None:
                            self.interface.tag_raise(self.gateOutputSprites[i2][i][i3])
                    self.interface.tag_raise(self.gateBindingSprites[i2][i])
                    for direction in [globalVar.N,globalVar.NE,globalVar.SE,globalVar.S,globalVar.SW,globalVar.NW]:
                        if self.inputPortSprites[i2][i][direction]!=None:
                            self.interface.tag_raise(self.inputPortSprites[i2][i][direction])
                            self.interface.tag_raise(self.inputPortCircles[i2][i][direction])
                        if self.outputPortSprites[i2][i][direction]!=None:
                            self.interface.tag_raise(self.outputPortSprites[i2][i][direction])
                            self.interface.tag_raise(self.outputPortCircles[i2][i][direction])