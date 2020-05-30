import map,globalVar


class gate:
    inputMap = [None]*6 #each index is an boolean argument, the content the direction of the input
    outputMap = [None]*6 #same, but for output
    memory = None #use to check circuit stability

    def __init__(self,x,y):
        self.x = x
        self.y = y

    def execute(self):
        print(self.__class__.__name__ + " at " + str(self.x) + "," + str(self.y) + " executed")

        canExecute = 1
        if(self.__class__.__name__ not in ["off","on"]):
            for i in range(self.inputAmount):
                if(globalVar.valueMap[self.x][self.y][self.inputMap[i]] == None):
                    canExecute = 0

        if(canExecute == 1):
            self.write(self.function(self.read()))

    def read(self):
        #getting all values
        values = []

        for i in range(self.inputAmount):
            values.append(globalVar.valueMap[self.x][self.y][self.inputMap[i]])

        return values

    def write(self,values):
        #writting the values gotten from the gate's function
        toWrite = [values[i] for i in range(self.outputAmount)]

        for i in range(self.outputAmount):
            xTarget = map.mapHandler.neighbor(self.x,self.y,self.outputMap[i])[0]
            yTarget = map.mapHandler.neighbor(self.x,self.y,self.outputMap[i])[1]
            sideTarget = map.mapHandler.neighbor(self.x,self.y,self.outputMap[i])[2]
            globalVar.valueMap[xTarget][yTarget][sideTarget] = 1

            if(globalVar.gateMap[xTarget][yTarget] != None):
                globalVar.gateMap[xTarget][yTarget].execute()

    def setInput(self,index,direction):
        self.inputMap[index] = direction

    def setOutput(self,index,direction):
        self.outputMap[index] = direction




class wire(gate):
    inputAmount = 1
    outputAmount = 1
    port = [None]*6

    def function(self,input):
        return [input[0]]

    def execute():
        print(self.__class__.__name__ + " at " + str(self.x) + "," + str(self.y) + " executed")
        #overcharge execute (wires are more dynamic port wise)
        if(self.inputMap[0] != None): #If the gate doesn't have a defined input
            for i in range(6):
                if(globalVar.valueMap[x,y,i] != None):
                    self.inputMap = i
        else:
            pass #To Be Done! Exception : Wire cannot implicitely deal with multiple inputs



class off(gate):
    inputAmount = 0
    outputAmount = 1

    def function(self,input):
        return [False]

class on(gate):
    inputAmount = 0
    outputAmount = 1

    def function(self,input):
        return [True]

class debugger(gate):
    inputAmount = 1
    outputAmount = 0

    def function(self,input):
        print(str(input))
        return []


