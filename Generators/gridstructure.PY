import random
import copy
class grid():
    def __init__(self,x:int,y:int) -> None: #please use odd numbered grids
        self.x_dim:int = 2*x+1
        self.y_dim:int = 2*y+1
        self.EmptyTiles:list = [] #This refers to Empty cells initially
        self.GridHolder:dict = {} #Base, isnt really used
        self.GridHolderFinal:dict = {}
        self.all_dir:tuple = (0,1,2,3) #("up","left","down","right") #This is now not stupid. Nice
        self.ProcessingGrid:dict = {}  #Essentially Midway work Grid, Grid base is base grid and grid final is result
        self.TypeList:list = ["Empty","Wall","Edge","PLACEHOLDER"]
        self.UnFUniversal:list = [] #Basically Base Mapped to Unfinalized keys (processing keys)
        self.UnFEmpty:list = [] #It is a list of keys local to this function, which sets coords to finalized if the Finalizing Wilson Sequence occurs: NOTE This uses USEFULTILES Coords (They all are empty at this stage)
        self.MoveDir:str = "" #Needed to be predefined for ChooseDir() to work
        self.EndGenerationStep1:bool = False #So that i dont run the gen loop 10000 times
        #Empty Serves as finalized, wall is counted as unfinalized until i Feel like it should be finallzed *I have no idea how to do this properly w/o turning whole grid empty
    def SetGridBase(self) -> None:
        for j in range(0,self.y_dim): #Adds cells to Maze grid, Empty Base Walls
          for i in range(0,self.x_dim):
            self.GridHolder[(i,j)] = cell()
            if (i % 2 == 0 and j % 2 == 0) or (i in [0,self.x_dim-1]) or (j in [0,self.y_dim-1]):  self.GridHolder[(i,j)].TypeSet("Wall")
            elif (i%2 == 0 and j%2 ==1) or (i%2 == 1 and j%2 ==0): self.GridHolder[(i,j)].TypeSet("Edge")
            else: 
                self.GridHolder[(i,j)].TypeSet("Empty")
                self.EmptyTiles.append(((i-1)/2,(j-1)/2))         
        self.ProcessingGrid = copy.deepcopy(self.GridHolder)
        xytuple:tuple = self.GetRandEmpty() #Adds Initial Point for generation: Is converted into Tile Keys next
        x:int = (xytuple[0]-1)/2 #x,y represent current x,y
        y:int = (xytuple[1]-1)/2 #Crude conversion to Empty tiles coordinates
        self.ProcessingGrid[(2*x+1,2*y+1)].Finalized = True
        #Figure out a way to create a new object(unique address) of GridHolder and use that to create GridHolderFinal
        #Grid Final wont be needed as in processing a create a new grid which will be used to update old dictionary 
    def ViewBase(self,clean:bool = False) -> None:
        for j in range(0,self.y_dim): #The i,j ordering is correct, if you think otherwise think again
            for i in range(0,self.x_dim):
                CellObject:cell = self.GridHolder[(i,j)]
                if CellObject.Type == "Wall":
                    print("🟨 ",end = "")
                elif CellObject.Type == "Empty" and CellObject.Finalized == False and (i,j) not in self.UnFUniversal:
                    print("🟦 ",end = "") #Unprocessed
                elif (CellObject.Finalized == True):
                    print("🔷 ", end= "") #Final
                elif (i,j) in self.UnFUniversal:
                    print("🟧 ", end= "") #Processing
                elif CellObject.Type == "Edge":
                    print("🟩 ",end ="")
                if clean == False:
                    print((i,j),end="")
            print()
        print("\n\n\n")
    def ViewProcessed(self,clean:bool = False) -> None:
        try:
            for j in range(0,self.y_dim): #The i,j ordering is correct, if you think otherwise think again
                for i in range(0,self.x_dim):
                    CellObject:cell = self.ProcessingGrid[(i,j)]
                    if CellObject.Type == "Wall":
                        print("🟨 ",end = "")
                    elif CellObject.Type == "Empty" and CellObject.Finalized == False and (i,j) not in self.UnFUniversal:
                        print("🟦 ",end = "") #Unprocessed
                    elif (CellObject.Finalized == True):
                        print("🔷 ", end= "") #Final
                    elif (i,j) in self.UnFUniversal:
                        print("🟧 ", end= "") #Processing
                    elif CellObject.Type == "Edge":
                        print("🟩 ",end ="")
                    if clean == False:
                        print((i,j),end="")
                print()
            print("\n")
        except AttributeError:
          print("Processing Grid Object Not Found (Generation is Complete)")  
    def ViewFinal(self,clean:bool = False) -> None:
        for j in range(0,self.y_dim):
            for i in range(0,self.x_dim):
                CellObject:cell = self.GridHolderFinal[(i,j)]
                if CellObject.Type == "Wall":
                    print("🟨 ",end = "")
                elif CellObject.Type == "Empty" and CellObject.Finalized == False and (i,j) not in self.UnFUniversal:
                    print("🟦 ",end = "") #Unprocessed
                elif (CellObject.Finalized == True):
                    print("🔷 ", end= "") #Final
                elif (i,j) in self.UnFUniversal:
                    print("🟧 ", end= "") #Processing
                elif CellObject.Type == "Edge":
                    print("🟩 ",end ="")
                if clean == False:
                    print((i,j),end="")
            print()
        print("\n\n\n")
    def GetAllType(self, Type) -> list: #Fetches all the keys for cells w/ a specified type #Also Unfinalized are only accessed #Also Only calls from Processing Grid
        ChoiceList:list = []
        for i in self.ProcessingGrid.keys():
            CellObject:cell = self.ProcessingGrid[(i[0],i[1])]
            if CellObject.Type == Type and CellObject.Finalized == False:
                ChoiceList.append(i)
        return ChoiceList
    def GetRandEmpty(self) -> tuple: #Returns a coords of a random "Empty" space (key) (For Processing Grid only)
        ListEmpty:list = self.GetAllType("Empty")
        if ListEmpty == []:
            return None
        return random.choice(ListEmpty)
    def ChooseDir(self,x:int,y:int) -> int: #albeit being int, int here only is a code: 0 1 2 3 -> up left down right 
        dir:list = []
        ValidKeys = copy.deepcopy(self.EmptyTiles)
        if (x,y+1) in ValidKeys and self.MoveDir != 2:
            dir.append(self.all_dir[0])
        if (x-1,y) in ValidKeys and self.MoveDir != 3:
            dir.append(self.all_dir[1])
        if (x,y-1) in ValidKeys and self.MoveDir != 0:
            dir.append(self.all_dir[2])
        if (x+1,y) in ValidKeys and self.MoveDir != 1:
            dir.append(self.all_dir[3])
        return random.choice(dir)
    def DirToKey(self,Dir:int,Coord:list) -> tuple: #Returns Next Coordinate according Input direction.
        if Dir == 0:
            Coord[1] += 1
        if Dir == 1:
            Coord[0] -= 1
        if Dir == 2:
            Coord[1] -= 1
        if Dir == 3:
            Coord[0] += 1
        return Coord
    def GenMaze_Step1(self) -> None: #Wilson Algorithm for Mazes
        xytuple:tuple = self.GetRandEmpty() #Adds Initial Point for generation: Is converted into Tile Keys next
        if xytuple == None: #Essentially if all tiles are finalized, it returns None and thus Gen function ends.
            self.EndGenerationStep1 = True
            return
        x:int = (xytuple[0]-1)/2 #x,y represent current x,y
        y:int = (xytuple[1]-1)/2 #Crude conversion to Empty tiles coordinates
        self.UnFEmpty.append((x,y))
        self.UnFUniversal.append((2*x+1,2*y+1))
        while 1>0:
            self.MoveDir = self.ChooseDir(x,y) #Essentially Chooses a dir, and then moves accordingly in proceeding lines    
            x2,y2 = self.DirToKey(self.MoveDir,[x,y]) #It is first stored in x2 y2 just to get the Edge cell inbetween and add it to list.
            CorrespondingCell:cell = self.ProcessingGrid[(2*x2+1,2*y2+1)]
            self.UnFEmpty.append((x2,y2))
            self.UnFUniversal.append((2*x2+1,2*y2+1))
            self.UnFUniversal.append((x+x2+1,y+y2+1)) #This refers to Edge cell in between
            x = copy.deepcopy(x2)
            y = copy.deepcopy(y2)
            if CorrespondingCell.Finalized == True:
                for i in self.UnFUniversal:
                    Cell:cell = self.ProcessingGrid[i]
                    Cell.Finalized = True
                    if Cell.Type == "Edge": Cell.Type = "Empty"
                del self.UnFEmpty[0:]
                del self.UnFUniversal[0:]
                break
            elif self.UnFEmpty.count((x2,y2)) > 1:
                del self.UnFEmpty[1:]
                del self.UnFUniversal[1:]
                x = self.UnFEmpty[0][0]
                y = self.UnFEmpty[0][1] 
    def GenMaze_Step2(self) -> None: #Make Walls Final, Make Edges Final and Walls. Calls Final Step after done
        for i in self.GetAllType("Wall"):
            CellObject:cell = self.ProcessingGrid[i]
            CellObject.Finalized = True
        for i in self.GetAllType("Edge"):
            CellObject:cell = self.ProcessingGrid[i]
            CellObject.Finalized = True
            CellObject.Type = "Wall"
        self.GenMaze_StepFinal()
    def GenMaze_StepFinal(self) -> None: #Just load Processing grid onto GridHolderFinal and Dump Processing grid
        self.GridHolderFinal = copy.deepcopy(self.ProcessingGrid)
        del self.ProcessingGrid
class cell(): #Cells are fundamental units of a maze grid: Wall is permanent, Edge is a way to differentiate cells, will finalize to walls.
    def __init__(self,Type:str="PLACEHOLDER",Weight:float=0):
        self.TypeList:list = ["Empty","Wall","Edge","PLACEHOLDER"]
        self.TypeSet(Type)
        self.Weight:float = Weight #For events 
        self.Finalized:bool = False #Used to check if tile is iterated
    def TypeSet(self,Type) -> None:
        if Type in self.TypeList:
            self.Type = Type
        else:
            print("Invalid Type Given: Replacing with placeholder.")
            self.Type = "PLACEHOLDER"
    def Info(self) -> None:
        print("Type:",self.Type,"\nFinalized:",self.Finalized,"\nWeight:",self.Weight)
x = int(input("Width: "))
y = int(input("Breadth: ")) #it would be nice if this all was implemented into the class
Maze = grid(x,y)
Maze.SetGridBase()
p = random.choice([1,2,3,4,5,6,7])
for i in range(1,1000): #Please Put this into the class: So as to measure how much is done and make % not a troll and use that % value to switch b/w generation algorithms
    Maze.GenMaze_Step1() == True    
    if i % 10 == 0:
        print(f"Processing code... {p}% Done") #Percentage is a troll cuz it looks good LOL
        p += random.choice([1,2,3,4,5,6,7])
    if Maze.EndGenerationStep1 == True:
        Maze.GenMaze_Step2()
        print("Processing code... 100% Done")
        break
Maze.ViewFinal(True) #True -> Clean Result (No Coordinates)