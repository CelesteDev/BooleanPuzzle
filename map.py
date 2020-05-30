import globalVar,gate

class mapHandler:
    def create(width,lenght):
        globalVar.valueMap = [[[None for i in range(6)] for j in range(lenght)] for k in range(width)]
        globalVar.gateMap = [[None for j in range(lenght)] for k in range(width)]

        globalVar.width = width
        globalVar.lenght = lenght

    def editTile(x,y,gate):
        globalVar.gateMap[x][y] = gate(x,y)

    def stepSim():
        for i in range (globalVar.width):
            for j in range (globalVar.lenght):
                if(globalVar.gateMap[i][j] != None):
                    if(globalVar.gateMap[i][j].__class__.__name__ in ['off','on']):
                        globalVar.gateMap[i][j].execute()


    def neighbor(x,y,direction):
        if(x%2==0):
            if(direction==globalVar.NE):
                return[x+1,y-1,globalVar.SW]
            if(direction==globalVar.SE):
                return[x+1,y,globalVar.NW]
            if(direction==globalVar.SW):
                return[x-1,y,globalVar.NE]
            if(direction==globalVar.NW):
               return[x-1,y-1,globalVar.SE]
        else:
            if(direction==globalVar.NE):
                return[x+1,y,globalVar.SW]
            if(direction==globalVar.SE):
                return[x+1,y+1,globalVar.NW]
            if(direction==globalVar.SW):
                return[x-1,y+1,globalVar.NE]
            if(direction==globalVar.NW):
                return[x-1,y,globalVar.SE]

        if(direction==globalVar.S):
            return[x,y+1,globalVar.N]
        if(direction==globalVar.N):
            return[x,y-1,globalVar.S]


if __name__ == "__main__":
    mapHandler.create(2,3)
    mapHandler.editTile(0,2,gate.off)
    globalVar.gateMap[0][2].setOutput(0,globalVar.NE)

    mapHandler.editTile(1,1,gate.debugger)
    globalVar.gateMap[1][1].setInput(0,globalVar.SW)

    mapHandler.stepSim()