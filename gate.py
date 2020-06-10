import map,globalVar


class gate:

    def __init__(self,x,y):
        self.x = x
        self.y = y
        self.inputMap = [None]*6 #each index is an boolean argument, the content the direction of the input
        self.outputMap = [None]*6 #same, but for output
        self.ready = False #if gate got all its inputs defined
        self.memory = [None]*6 #use to check circuit stability

    def execute(self):
        print(self.__class__.__name__ + " at " + str(self.x) + "," + str(self.y) + " executed")

        self.ready = True
        #if(self.__class__.__name__ not in ["off","on"]): #gate such as those are initializer gates (no need for input to be defined to execute) => outdated?

        for i in range(self.inputAmount):
            if(globalVar.valueMap[self.x][self.y][self.inputMap[i]] == None): #if all the inputs aren't defined, then the gate is not ready (note the we can't use "if None in" as the input map doesn't cover all the sides!)
                self.ready = False


        self.write(self.function(self.read()))

    def read(self):
        #getting all values
        values = []

        for i in range(self.inputAmount):
            values.append(globalVar.valueMap[self.x][self.y][self.inputMap[i]])
            if (values[i] == None): #if the input to get is not defined, default is False, though it's only for temporary use (gate not ready)
                values[i] = False

        print(str(self.__class__.__name__) + " at " + str(self.x) + "," + str(self.y) + " reads " + str(values))

        return values

    def write(self,values):
        #writting the values gotten from the gate's function
        toWrite = [values[i] for i in range(self.outputAmount)]

        for i in range(self.outputAmount):
            xTarget = map.mapHandler.neighbor(self.x,self.y,self.outputMap[i])[0]
            yTarget = map.mapHandler.neighbor(self.x,self.y,self.outputMap[i])[1]
            sideTarget = map.mapHandler.neighbor(self.x,self.y,self.outputMap[i])[2]
            globalVar.valueMap[xTarget][yTarget][sideTarget] = 1

            if(globalVar.gateMap[xTarget][yTarget] != None): #check if there is a gate to execute a the output
                globalVar.gateMap[xTarget][yTarget].execute()

        if(self.memory != [None] * 6): #if memory has been set
            if(toWrite != self.memory): #check if gate is unstable
                if(self.ready == True): #if gate should be considered as definitely defined
                    print("error, unstable gate!")

        self.memory = toWrite #defines memory
        print(str(self.__class__.__name__) + " at " + str(self.x) + "," + str(self.y) + " writes " + str(toWrite))

    def setInput(self,index,direction):
        self.inputMap[index] = direction

    def setOutput(self,index,direction):
        self.outputMap[index] = direction




class wire(gate):
    #this special gate doesn't need to check for stability
    
    def __init__(self,x,y):
        self.inputAmount=1
        self.outputAmount=0
        self.portMap = [False] * 6 #if port in use (potential input output)
        super(wire,self).__init__(x,y)

    def function(self,input):
        return [input[0]] * self.outputAmount

    def execute(self):
        print(self.__class__.__name__ + " at " + str(self.x) + "," + str(self.y) + " executed")
        #overcharge execute (wires are more dynamic port wise)
        if(self.inputMap[0] != None): #If the gate doesn't have a defined input
            for i in range(6): #finding the source of the execution
                if(globalVar.valueMap[self.x][self.y][i] != None):
                    if(self.portMap[i] == True): #if port connected
                        self.inputMap[i]= i
                        self.ready = 1 #here ready means something else, check if the input is assigned
        else:
            for i in range(6): #finding the source of the execution
                if(globalVar.valueMap[self.x][self.y][i] != None):
                    if(i not in self.inputMap):
                        print("Exception : Wire cannot implicitely deal with multiple inputs")


        for i in range(6):
            if(i in self.portMap):
                self.outputMap[self.outputAmount] = i
                self.outputAmount += 1

        if(self.ready == True):
            self.write(self.function(self.read()))

    def togglePort(self,direction):
        self.portMap[direction] = not(self.portMap[direction])



class off(gate):
    def __init__(self,x,y):
        self.inputAmount=0
        self.outputAmount=1
        super(off,self).__init__(x,y)

    def function(self,input):
        return [False]

class on(gate):
    def __init__(self,x,y):
        self.inputAmount=0
        self.outputAmount=1
        super(on,self).__init__(x,y)

    def function(self,input):
        return [True]

class negative(gate): #not
    def __init__(self,x,y):
        self.inputAmount=1
        self.outputAmount=1
        super(negative,self).__init__(x,y)

    def function(self,input):
        return [not input[0]]

class multiply(gate): #and
    def __init__(self,x,y):
        self.inputAmount=2
        self.outputAmount=1
        super(multiply,self).__init__(x,y)

    def function(self,input):
        return [input[0] and input[1]]

class add(gate): #or
    def __init__(self,x,y):
        self.inputAmount=2
        self.outputAmount=1
        super(add,self).__init__(x,y)

    def function(self,input):
        return [input[0] or input[1]]

class xor(gate):
    def __init__(self,x,y):
        self.inputAmount=2
        self.outputAmount=1
        super(xor,self).__init__(x,y)

    def function(self,input):
        return [input[0] != input[1]]

class debugger(gate):
    def __init__(self,x,y):
        self.inputAmount=1
        self.outputAmount=0
        super(debugger,self).__init__(x,y)

    def function(self,input):
        print("debug gate reports : " + str(input[0]))
        return []


