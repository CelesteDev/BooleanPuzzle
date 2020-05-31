import globalVar,gate

class mapHandler:
    def create(width,length):
        globalVar.valueMap = [[[None for i in range(6)] for j in range(length)] for k in range(width)]
        globalVar.gateMap = [[None for j in range(length)] for k in range(width)]

        globalVar.width = width
        globalVar.length = length

    def editTile(x,y,gate):
        globalVar.gateMap[x][y] = gate(x,y)

    def stepSim():
        for i in range (globalVar.width):
            for j in range (globalVar.length):
                if(globalVar.gateMap[i][j] != None):
                    if(globalVar.gateMap[i][j].__class__.__name__ in ['off','on']):
                        globalVar.gateMap[i][j].execute()


    def neighbor(x,y,direction):
        if(direction==globalVar.NE):
            return[x+1,y-1,globalVar.SW]
        if(direction==globalVar.SE):
            return[x+1,y,globalVar.NW]
        if(direction==globalVar.S):
            return[x,y+1,globalVar.N]
        if(direction==globalVar.SW):
            return[x-1,y+1,globalVar.NE]
        if(direction==globalVar.NW):
           return[x-1,y,globalVar.SE]
        if(direction==globalVar.N):
            return[x,y-1,globalVar.S]